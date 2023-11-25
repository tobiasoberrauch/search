import json
import os
from pydub import AudioSegment
from vosk import KaldiRecognizer, Model

def use_vosk(file_path, model_path):
    model = Model(model_path)
    audio = AudioSegment.from_mp3(file_path).set_frame_rate(16000).set_channels(1)
    recognizer = KaldiRecognizer(model, 16000)

    chunk_size = 4000  # Process 4 seconds at a time
    for i in range(0, len(audio), chunk_size):
        chunk = audio[i:i+chunk_size].raw_data
        recognizer.AcceptWaveform(chunk)
    
    return json.loads(recognizer.FinalResult())['text']

def process_directory(source_dir, target_dir, model_path):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.mp3'):
            file_path = os.path.join(source_dir, filename)
            result = use_vosk(file_path, model_path)
            target_file_path = os.path.join(target_dir, os.path.splitext(filename)[0] + '.txt')

            with open(target_file_path, 'w') as f:
                f.write(result)

source_dir = 'data/silver'
target_dir = 'data/gold'
model_path = 'models/vosk-model-en-us-0.22'
process_directory(source_dir, target_dir, model_path)
