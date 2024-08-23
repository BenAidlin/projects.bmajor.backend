from django.urls import path  
from . import views  
  
urlpatterns = [  
    path('upload/', views.upload_audio, name='upload_audio'),  
    path('record/', views.record_audio, name='record_audio'),
]  