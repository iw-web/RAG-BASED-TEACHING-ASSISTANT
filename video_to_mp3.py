import os
import sys
import subprocess

# MUST be at the very top, before any print statements
sys.stdout.reconfigure(encoding='utf-8')

files = os.listdir("videos")

for file in files:
    file_name=file.strip("|")[0]
    print(file_name)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{file_name}.mp3"])
   
   
 
     