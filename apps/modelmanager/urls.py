from django.urls import path
from . import views
app_name = 'modelmanager'

urlpatterns = [
    path('upload_ml_model',
         views.MLModelCreateView.as_view(),
         name='mlmodel_upload_url'
         ),
    path('ml_model_update/',
         views.MLModelUpdateView.as_view(),
         name='mlmodel_update_url'
         ),
    path('user/ml_model_list/',
         views.UserMLModelListView.as_view(),
         name='user_mlmodel_list_url'
         ),
    path('public/ml_model_list',
         views.PublicMLModelListView.as_view(),
         name='public_mlmodel_list_url'
         ),
]
