import json
import os
import wave

from vosk import KaldiRecognizer, Model



def use_vosk(file_path, model_path):
    model = Model(model_path)
    with wave.open(file_path, "rb") as wf:
        recognizer = KaldiRecognizer(model, wf.getframerate())
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                pass
        return json.loads(recognizer.FinalResult())['text']

def process_directory(source_dir, target_dir, model_path):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.wav'):
            file_path = os.path.join(source_dir, filename)
            result = use_vosk(file_path, model_path)
            target_file_path = os.path.join(target_dir, os.path.splitext(filename)[0] + '.txt')

            with open(target_file_path, 'w') as f:
                f.write(result)

source_dir = 'data/silver'
target_dir = 'data/gold'
model_path = 'models/vosk-model-en-us-0.22/vosk-model-en-us-0.22'
process_directory(source_dir, target_dir, model_path)
