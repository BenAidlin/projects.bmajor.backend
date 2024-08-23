from django.shortcuts import render  
from .forms import UploadFileForm  
from .utils import process_audio_file  
  
def upload_audio(request):  
    if request.method == 'POST':  
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():  
            audio_file = request.FILES['audio_file']  
            result = process_audio_file(audio_file)  
            return render(request, 'result.html', {'result': result})  
    else:  
        form = UploadFileForm()  
    return render(request, 'upload.html', {'form': form})  