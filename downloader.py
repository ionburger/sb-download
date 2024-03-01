import yt_dlp as ydl
import sponsorblock


opts = {"outtmpl": "downloads/%(id)s.%(ext)s"}
ydl = ydl.YoutubeDL(opts)
ydl.download("https://www.youtube.com/@LinusTechTips/videos")
