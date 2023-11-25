import os
import requests
from pytube import YouTube

# Set the channel ID
channels =  [
    'UChpleBmo18P08aKCIgti38g'
]

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

for channel_id in channels:

    # Set the API endpoint
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=50&key={GOOGLE_API_KEY}'

    # Send the API request
    response = requests.get(url)

    # Get the video data from the response
    videos = response.json().get('items', [])

    # Print the video titles
    for video in videos:
        if video['id']['kind'] == 'youtube#video':
            videoId = video['id']['videoId']
            url = f'https://www.youtube.com/watch?v={videoId}'
            print(f'download {url}')
            YouTube(url).streams.first().download(output_path=f'./data/bronze/{channel_id}')
