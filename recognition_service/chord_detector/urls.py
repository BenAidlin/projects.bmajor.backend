from django.urls import path  
from . import views  
from .views import UploadAudioView, RecordAudioView

urlpatterns = [  
    path('upload/', UploadAudioView.as_view(), name='upload_audio'),  
    path('record/', RecordAudioView.as_view(), name='record_audio'),
]  