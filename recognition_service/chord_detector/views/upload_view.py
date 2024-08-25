from django.shortcuts import render  
from django.views import View  
from ..forms import UploadFileForm  
from ..utils import process_audio_file  

# upload audio is an example using django's forms. not really applicable in a pure backend application
class UploadAudioView(View):  
    def get(self, request, *args, **kwargs):  
        form = UploadFileForm()  
        return render(request, 'upload.html', {'form': form})  
      
    def post(self, request, *args, **kwargs):  
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():  
            audio_file = request.FILES['audio_file']  
            result = process_audio_file(audio_file)  
            return render(request, 'result.html', {'result': result})  
        return render(request, 'upload.html', {'form': form})  