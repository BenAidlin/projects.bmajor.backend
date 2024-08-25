from django.shortcuts import render  
from django.views import View  
from ..utils import process_audio_file  
  
# record audio view is an example of not using django's forms. more applicable in a pure backend application
class RecordAudioView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'upload.html')  
      
    def post(self, request, *args, **kwargs):  
        file = request.FILES.get('file')  
        result = process_audio_file(file)  
        return render(request, 'result.html', {'result': result})  