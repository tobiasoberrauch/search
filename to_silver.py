import os
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    try:
        # Ensure the target directory exists
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
        
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path)
        return True
    except Exception as e:
        print(f"Error extracting audio from {video_path}: {e}")
        return False


directory = 'data/bronze'
extensions = ['.3gpp', '.mp4']

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(tuple(extensions)):
            file_path = os.path.join(root, file)
            wav_path = f'data/silver/{os.path.splitext(file)[0]}.wav'
            if extract_audio_from_video(file_path, wav_path):
                print(f"Audio extracted to {wav_path}")
            else:
                print(f"Failed to extract audio for {file_path}")
