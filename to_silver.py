import os
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    try:
        # Ensure the target directory exists
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
        
        video = VideoFileClip(video_path)
        # Specify codec for MP3 and set the file extension to .mp3
        video.audio.write_audiofile(output_audio_path, codec='libmp3lame')
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
            # Change the file extension to .mp3
            mp3_path = f'data/silver/{os.path.splitext(file)[0]}.mp3'
            if extract_audio_from_video(file_path, mp3_path):
                print(f"Audio extracted to {mp3_path}")
            else:
                print(f"Failed to extract audio for {file_path}")
