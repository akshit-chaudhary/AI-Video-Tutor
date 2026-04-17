import requests
import os
import json 
import numpy as np
import pandas as pd
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity  
# from read_chunks import create_embedding

def create_embedding(text_list):
    r=requests.post ( "http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input" : text_list
    })


    embedding=r.json()['embeddings']
    return embedding


def inference(prompt):
    r=requests.post ( "http://localhost:11434/api/generate",json={
        "model":"llama3.2",
        "prompt": prompt,
        "stream": False
    })
    response=r.json()
    return response
    # print(response)


df=joblib.load('embeddings.joblib')
incoming_queries=input("ask what u want: ")  
ques=create_embedding([incoming_queries])[0] 
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding']).shape)
similarity=cosine_similarity(np.vstack(df['embedding']),[ques]).flatten()
#print(similarity)

topresult=10
max_sp=similarity.argsort()[::-1][0:topresult]
# print (max_sp)

newdf = df.loc[max_sp].copy()
newdf["score"] = similarity[max_sp]
# print(newdf[["title","number","text","score"]])

prompt=f'''I am teaching ccat entrance exam.
You are an AI assistant helping a student preparing for the CCAT exam.
here are given video subtitle chunks with:
- video title
- video number
- start time (in seconds)
- end time (in seconds)
- text content

{newdf[["title","number","start","end","text"]].to_json(orient="records")}
----------------------------
User Question:
{incoming_queries}

INSTRUCTIONS (DO NOT SHOW THESE):
- Answer in simple, natural human language
- Keep answer short and helpful
- Focus on guiding user to video
- Provide top 2 most relevant video parts
- MUST include:
  • Video number
  • Start time and end time
- Do NOT use words like:
  "Main goal", "Instruction", "Explanation format"
- Do NOT sound robotic or structured like a report
- If unrelated → say you only answer course-related questions
'''
with open("prompt.text","w")as f:
    f.write(prompt)


result=inference(prompt)
print(result['response'])


with open("response.text","w")as f:
    f.write(result['response'])  

#print(inference(prompt))
# for index,item in newdf.iterrows():
#     print(index,item['title'],item['number'],item['text'],item['start'],item['end'])