from django.urls import path
from . import views

app_name = "detectobj"

urlpatterns = [
    path("<int:pk>/selected_image/",
         views.InferenceImageDetectionView.as_view(),
         name="detection_image_detail_url"
         ),
]
