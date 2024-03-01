import yt_dlp as ydl
import os

if os.path.exists("downloads") == False:
    os.mkdir("downloads")

opts = {
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "format": "best[height<=480][width<=640],best",
    "nooverwrites": True,
    "playlist-start": input("1 if you dont know what ur doing")
    }
ydl = ydl.YoutubeDL(opts)
ydl.download("https://www.youtube.com/@LinusTechTips/videos")
