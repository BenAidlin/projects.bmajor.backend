import librosa  
import soundfile as sf  
import tempfile  
from madmom.features.chords import DeepChromaChordRecognitionProcessor  
from madmom.audio.chroma import DeepChromaProcessor

def process_audio_file(file):  
    # Create a temporary file to store the uploaded audio content  
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio_file:  
        for chunk in file.chunks():  
            temp_audio_file.write(chunk)  
        temp_audio_file.flush()  
          
        # Use librosa to load the audio data from the temporary WAV file  
        y, sr = librosa.load(temp_audio_file.name, sr=None, mono=True)  
          
        # Ensure the audio data is a float32 NumPy array  
        y = y.astype('float32')  
          
        # Create another temporary file to store the audio data in WAV format for Madmom  
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_wav_file:  
            sf.write(temp_wav_file.name, y, sr)  
              
            # Now you can use the temporary WAV file path with madmom  
            dcp = DeepChromaProcessor()
            decode = DeepChromaChordRecognitionProcessor()
            chroma = dcp(temp_wav_file.name)  
            decoded = decode(chroma)
              
            return [(start, end, chord) for start, end, chord in decoded]  