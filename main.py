import yt_dlp as ydl
import sponsorblock
import moviepy.editor as mpy
import os

video = "https://www.youtube.com/watch?v=e-4RlKcinzc"
opts = {"outtmpl": "%(id)s.%(ext)s"}
ydl = ydl.YoutubeDL(opts)
ydl.download(video)

segments = []

sb = sponsorblock.Client()
for segment in sb.get_skip_segments(video):
    if segment.category == "sponsor":
        segments.append([segment.start, segment.end])

i = 0
clips = []
for segment in segments:
    i += 1
    clip = mpy.VideoFileClip(video.split("=")[1] + ".webm")
    clip = clip.subclip(segment[0], segment[1])
    clips.append(clip)

final_clip = mpy.concatenate_videoclips(clips)
final_clip.write_videofile(f"output/{video.split('=')[1]}.mp4")

os.remove(video.split("=")[1] + ".webm")

