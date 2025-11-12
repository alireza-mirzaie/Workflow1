import os
os.makedirs("out", exist_ok=True)
os.system("ffmpeg -loop 1 -i https://picsum.photos/720/1280 -i out/voice.mp3 -c:v libx264 -c:a aac -b:a 192k -shortest out/final_vertical.mp4 -y")
print("✅ Video rendered")
