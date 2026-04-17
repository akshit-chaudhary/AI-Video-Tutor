import whisper
import os
import json

model=whisper.load_model("small")
audio=os.listdir("audio")
for audi in audio:
    #print(audi)
    if not audi.endswith(".mp3"):
        continue
    if "_" not in audi:
        continue

    number=audi.split("_")[0]
    title=audi.split("_")[1][:-4] 
    print(number,title)
    result=model.transcribe(audio=f"audio/{audi}",
                           language="hi",
                           task="translate",
                           word_timestamps=False)
    chunks=[]
    for segament in result["segments"]:
        chunks.append({"number":number,"title":title,"start":segament["start"],"end":segament["end"],"text":segament["text"]})
    chunks_w_m={"chunks":chunks,"text":result["text"]}
    #print(chunks)
    with open (f"json/{audi}.json","w")as f:
        json.dump(chunks_w_m,f)
