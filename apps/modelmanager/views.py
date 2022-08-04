from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import MLModel


class MLModelUploadView(LoginRequiredMixin, CreateView):
    model = MLModel
    fields = ['pth_file', 'class_file',
              'description', 'model_version', 'public']

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        form.save(commit=False)
        if not MLModel.objects.filter(name=form.instance.pth_filename).exists():
            form.instance.name = form.instance.pth_filename
            if not MLModel.objects.filter(class_filename=form.instance.cls_filename).exists():
                form.instance.class_filename = form.instance.cls_filename
            messages.success(self.request,
                             f'Pre-trained model {form.instance.pth_filename} uploaded successfully.'
                             )
            return super().form_valid(form)
        else:
            messages.error(self.request,
                           f'Ml Model with the name {form.instance.name}, already exists in the database.'
                           )
            form.add_error(
                'pth_file',
                f'Ml Model with the nem {form.instance.name}, already exists in the database.'
            )
            context = {
                'form': form
            }
            return render(self.request, 'modelmanager/mlmodel_form.html', context)


class UserMLModelListView(LoginRequiredMixin, ListView):
    model = MLModel
    context_object_name = 'user_models'
    template_name: str = 'modelmanager/usermlmodel_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(uploader=self.request.user)


class PublicMLModelListView(LoginRequiredMixin, ListView):
    model = MLModel
    context_object_name = 'public_models'
    template_name: str = 'modelmanager/usermlmodel_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(public=True)
