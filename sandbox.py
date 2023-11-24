import whisper

model = whisper.load_model("base")
result = model.transcribe("data/silver/AI Plays Pokemon with Reinforcement Learning.wav")
print(result["text"])
