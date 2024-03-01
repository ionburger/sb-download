import os
import moviepy as mpy

while True:
    clips = []
    length = 0

    for file in os.listdir("clips"):
        if length > 3600:
            final_clip = moviepy.editor.concatenate_videoclips(clips)
            final_clip.write_videofile("final.mp4")
        clip = mpy.VideoFileClip(f"clips/{file}")
        length += clip.duration
        clips.append(clip)
        os.remove(f"clips/{file}")
