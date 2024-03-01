import moviepy as mpy
import sponsorblock as sb
import os
import time

sb = sponsorblock.Client()

if os.path.exists("downloads") == False:
        os.mkdir("downloads")

while True:
    if not os.listdir("downloads"):
        print("[INFO][CUTTER] No videos to cut. Waiting for new videos...")
        time.sleep(10)
    else:
        segments = []
        video = os.listdir("downloads")[0]
        print(f"[INFO][CUTTER] Found {video}...")

        for segment in sb.get_skip_segments(f"https://www.youtube.com/watch?v={video}"):
            if segment.category == "sponsor":
                segments.append([segment.start, segment.end])
        
        if segments:
            print(f"[INFO][CUTTER] Found {len(segments)} segments...")
            i = 1
            for segment in segments:
                print(f"[INFO][CUTTER] Cutting segment {i}...")
                clip = mpy.VideoFileClip(f"downloads/{video}")
                clip = clip.subclip(segment[0], segment[1])
                clip.write_videofile(f"output/{video}.webm")
                clip.close()
                os.remove(f"downloads/{video}{i}")
                i += 1
                print(f"[INFO][CUTTER] Done!")

        else:
            print("[WARN][CUTTER] No segments found. Skipping...")
