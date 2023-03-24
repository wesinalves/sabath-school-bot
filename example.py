from googleapiclient.discovery import build
import json

with open('key.json') as f:
    keys = json.load(f)
    api_key = keys['api_key']

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="lição da escola sabatina 23/03/2023"
    )
response = request.execute()

def get_video(search, channel_id, data):
    # return title, url, chanel_name?
    pass
