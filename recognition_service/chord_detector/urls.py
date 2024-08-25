from django.urls import path  
from . import views  
from .views import UploadAudioView

urlpatterns = [  
    path('upload/', UploadAudioView.as_view(), name='upload_audio'),  
]  