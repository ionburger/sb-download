import yt_dlp as ydl
import os

if os.path.exists("downloads") == False:
    os.mkdir("downloads")

opts = {
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "format": "best[height<=480][width<=640],best",
    "nooverwrites": True
    }
ydl = ydl.YoutubeDL(opts)
ydl.download("https://www.youtube.com/@LinusTechTips/videos")
