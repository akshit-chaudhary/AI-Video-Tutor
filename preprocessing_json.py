import requests
import os
import json 
import numpy as np
import pandas as pd
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  

def create_embedding(text_list):
    r=requests.post ( "http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input" : text_list
    })


    embedding=r.json()['embeddings']
    return embedding
# a=create_embedding(["lmt is good","ccat is easy"])
# print(a)

jsons=os.listdir("newjsons")
mydis=[]
chunk_id=0
 


for json_file in jsons:
    if not json_file.endswith(".json"):
        continue

    with open(f"newjsons/{json_file}")as f:
        content=json.load(f)

    print(f"Creating embedding for {json_file}")    
    embeddings=create_embedding([c['text'] for c in content['chunks']])


    for i,chunk in enumerate( content['chunks']):
        #print(chunk)
        chunk['chunk_id']=chunk_id
        chunk['embedding']=embeddings[i]
        chunk_id+=1 
        mydis.append(chunk)
   # break          
#print(mydis)    


df=pd.DataFrame.from_records(mydis)
joblib.dump(df,'embeddings.joblib')
# print(df)  
# incoming_queries=input("ask what u want: ")  
# ques=create_embedding([incoming_queries])[0] 
# # print(np.vstack(df['embedding'].values))
# # print(np.vstack(df['embedding']).shape)
# similarity=cosine_similarity(np.vstack(df['embedding']),[ques]).flatten()
# print(similarity)
# max_sp=similarity.argsort()[::-1][0:3]
# print (max_sp)
# newdf=df.loc[max_sp]
# print(newdf[["title","number","text"]])