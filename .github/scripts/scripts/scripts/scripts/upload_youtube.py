from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import sys, os

creds = Credentials(
    None,
    refresh_token=os.environ['YT_REFRESH_TOKEN'],
    token_uri='https://oauth2.googleapis.com/token',
    client_id=os.environ['YT_CLIENT_ID'],
    client_secret=os.environ['YT_CLIENT_SECRET']
)

youtube = build('youtube', 'v3', credentials=creds)
file_path, title, desc = sys.argv[1:4]

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {"title": title, "description": desc, "categoryId": "28"},
        "status": {"privacyStatus": "public"}
    },
    media_body=file_path
)
request.execute()
print("✅ Uploaded to YouTube")
