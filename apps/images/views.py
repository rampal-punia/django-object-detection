from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ImageSet, ImageFile


class ImageSetCreateView(LoginRequiredMixin, CreateView):
    model = ImageSet
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ImageSetListView(LoginRequiredMixin, ListView):
    model = ImageSet
    context_object_name = 'imageset_qs'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ImageSetDetailView(LoginRequiredMixin, DetailView):
    model = ImageSet
    context_object_name = 'imageset'


class ImagesUploadView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        imageset_id = self.kwargs.get("pk")
        imageset = get_object_or_404(ImageSet, id=imageset_id)
        context = {
            'imageset': imageset,
        }
        return render(request, 'images/imagefile_form.html', context)

    def post(self, request, *args, **kwargs):
        imageset_id = self.kwargs.get("pk")
        imageset = get_object_or_404(ImageSet, id=imageset_id)
        if self.request.method == 'POST':
            images = [self.request.FILES.get("file[%d]" % i)
                      for i in range(0, len(self.request.FILES))]
            for img in images:
                ImageFile.objects.create(image=img, image_set=imageset)

            message = f"Uploading images to the Imageset: {imageset}. \
                Automatic redirect to the images list after completion."

            redirect_to = reverse_lazy(
                "images:images_list_url", args=[imageset.id])
            return JsonResponse({"result": "result",
                                "message": message,
                                 "redirect_to": redirect_to,
                                 "files_length": len(images),
                                 },
                                status=200,
                                content_type="application/json"
                                )


class ImagesListView(LoginRequiredMixin, ListView):
    model = ImageFile
    context_object_name = 'images'

    def get_queryset(self):
        imageset_id = self.kwargs.get('pk')
        return super().get_queryset().filter(image_set__id=imageset_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        imageset_id = self.kwargs.get('pk')
        imageset = get_object_or_404(ImageSet, id=imageset_id)
        context["imageset"] = imageset
        return context


class DetectObjectView(LoginRequiredMixin, DetailView):
    model = ImageFile
    context_object_name = 'image_qs'
    template_name: str = 'images/detect_object.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.get_object()
        imageset = get_object_or_404(ImageSet, id=self.kwargs.get('imgset_pk'))
        images = imageset.images.all()
        context["image"] = image
        context["imageset"] = imageset
        context["images"] = images
        return context


class ImagesDeleteUrl(LoginRequiredMixin, DeleteView):
    model = ImageFile

    def get_success_url(self):
        qs = self.get_object()
        return qs.get_delete_url()
