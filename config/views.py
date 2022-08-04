from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
