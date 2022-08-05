import os
import io
from PIL import Image as I
import torch
import collections
from ast import literal_eval

from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

from images.models import ImageFile
from .models import ImageDetection
from .forms import ImageDetectionForm, ModelConfidenceForm
from modelmanager.models import MLModel


class DetectionImageDetailView(LoginRequiredMixin, DetailView):
    model = ImageFile
    template_name = "detectobj/selected_image.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        img_qs = self.get_object()
        imgset = img_qs.image_set
        images_qs = imgset.images.all()
        paginator = Paginator(images_qs, 20)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context["img_qs"] = img_qs
        context["is_paginated"] = True if images_qs.count() > 50 else False
        context["page_obj"] = page_obj
        context["form"] = ImageDetectionForm()
        context["form2"] = ModelConfidenceForm()
        return context

    def post(self, request, *args, **kwargs):
        img_qs = self.get_object()
        img_bytes = img_qs.image.read()
        img = I.open(io.BytesIO(img_bytes))
        selected_detection_model_id = self.request.POST.get("custommodel")
        modelconf = self.request.POST.get("confidence")
        if modelconf:
            modelconf = float(modelconf)
        else:
            modelconf = 0.45
        selected_detection_model = MLModel.objects.get(
            id=selected_detection_model_id)
        selected_detection_model_name = selected_detection_model.name
        base_dir = settings.BASE_DIR
        yolo_folder = os.path.join(base_dir, "yolov5")
        # torch.cuda.empty_cache()
        model = torch.hub.load(
            yolo_folder,
            'custom',
            path=f"{yolo_folder}/weights/{selected_detection_model_name}.pt",
            source='local',
            force_reload=True,
        )
        model.conf = modelconf
        results = model(img, size=640)
        results_list = results.pandas().xyxy[0].to_json(orient="records")
        results_list = literal_eval(results_list)
        classes_list = [item["name"] for item in results_list]
        results_counter = collections.Counter(classes_list)
        if results_list == []:
            messages.warning(
                request, f'Model "{selected_detection_model_name}" unable to predict. Try another model.')
        else:
            results.render()
            media_folder = settings.MEDIA_ROOT
            inferrenced_img_dir = os.path.join(
                media_folder, "inferrenced_image")
            if not os.path.exists(inferrenced_img_dir):
                os.makedirs(inferrenced_img_dir)
            for img in results.imgs:
                img_base64 = I.fromarray(img)
                img_base64.save(
                    f"{inferrenced_img_dir}/{img_qs}.jpg", format="JPEG")
        torch.cuda.empty_cache()
        # Ready for rendering next image on same html page.
        imagset = img_qs.image_set
        images_qs = imagset.images.all()
        paginator = Paginator(images_qs, 50)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # inferrenced_img_qs =

        context = {}
        context["img_qs"] = img_qs
        context["page_obj"] = page_obj
        context["is_paginated"] = True if images_qs.count() > 50 else False
        context["form"] = ImageDetectionForm()
        context["inferrenced_img_dir"] = f"{settings.MEDIA_URL}inferrenced_image/{img_qs.name}.jpg"
        context["results_list"] = results_list
        context["results_counter"] = results_counter
        context["form2"] = ModelConfidenceForm()
        return render(request, "detectobj/selected_image.html", context)
