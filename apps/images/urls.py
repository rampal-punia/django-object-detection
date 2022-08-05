from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create_image_set/', views.ImageSetCreateView.as_view(),
         name='imageset_create_url'),

    path('<int:pk>/update_image_set/', views.ImageSetUpdateView.as_view(),
         name='imageset_update_url'),

    path('image_set_list/', views.ImageSetListView.as_view(),
         name='imageset_list_url'),

    path('<int:pk>/imageset/', views.ImageSetDetailView.as_view(),
         name='imageset_detail_url'),

    path('<int:pk>/upload_images/', views.ImagesUploadView.as_view(),
         name='upload_images_url'),

    path('<int:pk>/images_list/', views.ImagesListView.as_view(),
         name='images_list_url'),

    path('<int:imgset_pk>/delete_image/<int:pk>/', views.ImagesDeleteUrl.as_view(),
         name='image_delete_url'),
]
