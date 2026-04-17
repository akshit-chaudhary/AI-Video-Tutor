import whisper
import json
model =whisper.load_model("small")
result=model.transcribe(audio="audio/sample video.mp3",
                        language="hi",
                        task="translate")
print(result["segments"])
chunks=[]
for segament in result["segments"]:
    chunks.append({"start":segament["start"],"end":segament["end"],"text":segament["text"]})
print(chunks)
with open ("output.json","w")as f:
    json.dump(chunks,f)