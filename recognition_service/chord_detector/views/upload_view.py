from django.http import JsonResponse
from django.shortcuts import render  
from django.views import View  
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..utils import process_audio_file  

@method_decorator(csrf_exempt, name='dispatch') 
class UploadAudioView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'upload.html')  
      
    def post(self, request, *args, **kwargs):  
        audio_file = request.FILES.get('file')  
        if audio_file:  
            result = process_audio_file(audio_file)  
            return JsonResponse({'result': result})  
        return JsonResponse({'error': 'Invalid file'}, status=400)  