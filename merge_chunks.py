import os
import json
import math
n=5

for filename in os.listdir("jsons"):
    if filename.endswith(".json"):
        file_path=os.path.join("jsons",filename)
        with open(file_path,'r',encoding="utf-8")as f:
            data=json.load(f)

        newchunk=[]
        num_chunk=len(data["chunks"])
        grp_chunk=math.ceil(num_chunk / n)

        for i in range(grp_chunk):
            stridx=i*n
            endidx=min((i+1)*n,num_chunk)
            chunkgrp=data['chunks'][stridx:endidx]

            newchunk.append({
                "number":data['chunks'][0]['number'],
                "start":chunkgrp[0]['start'],
                "end":chunkgrp[-1]['end'],
                "title":chunkgrp[0]['title'],
                "text":" ".join(c['text'] for c in chunkgrp )

            })
        os.makedirs("newjsons",exist_ok=True)
        with open(os.path.join("newjsons", filename) ,"w",encoding="utf-8")as json_file:
            json.dump({"chunks": newchunk, "text": data['text']}, json_file, indent=4)