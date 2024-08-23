from madmom.features.chords import DeepChromaChordRecognitionProcessor  
  
def process_audio_file(file):  
    processor = DeepChromaChordRecognitionProcessor()  
    chords = processor(file)  
    return [(timestamp, chord) for timestamp, chord in chords]  