from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from images.models import ImageSet


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_imagesets = ImageSet.objects.filter(user=user)
        public_imagesets = ImageSet.objects.filter(public=True)
        context["user_imagesets"] = user_imagesets
        context["public_imagesets"] = public_imagesets
        return context
