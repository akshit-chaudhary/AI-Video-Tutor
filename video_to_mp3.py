import os
import subprocess
files=os.listdir("videos")
#print(files)
for file in files:
    #print(file)
    if file.startswith("."):
        continue
    tutorial_no=file.split(".")[0].split("-")[1]
    filename=file.split("-")[0]
    print(tutorial_no,filename)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audio/{tutorial_no}_{filename}.mp3"])