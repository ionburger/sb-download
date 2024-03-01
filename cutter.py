from moviepy import editor as mpy
import sponsorblock
import os
import time

sb = sponsorblock.Client()

if os.path.exists("clips") == False:
        os.mkdir("clips")

while True:
    if not os.listdir("downloads"):
        print("No videos to cut. Waiting for new videos...")
        time.sleep(10)
    else:
        segments = []
        video = os.listdir("downloads")[0].split("!")[0]
        print(f"Found {video}...")

        for segment in sb.get_skip_segments(f"https://www.youtube.com/watch?v={video}"):
            if segment.category == "sponsor":
                segments.append([segment.start, segment.end])
        
        if segments:
            print(f"Found {len(segments)} segments...")
            i = 1
            for segment in segments:
                print(f" Cutting segment {i}...")
                clip = mpy.VideoFileClip(f"downloads/{video}")
                clip = clip.subclip(segment[0], segment[1])
                clip.write_videofile(f"clips/{video}-{i}.webm")
                clip.close()
                i += 1
                print(f" Done!")
            os.remove(f"downloads/{video}")
        else:
            print("No segments found. Skipping...")
