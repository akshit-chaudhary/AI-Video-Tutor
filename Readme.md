# 🎥 AI Video Tutor (RAG-Based Learning Assistant)

An AI-powered learning assistant that helps students find **exact video timestamps** for their questions using **Retrieval-Augmented Generation (RAG)**.

Instead of giving long explanations, this system guides users to the **most relevant part of a video** to learn efficiently.

---

## 🚀 Features

- 🔍 Semantic search using embeddings (bge-m3)
- 🤖 LLM-powered answers using LLaMA (via Ollama)
- 🎯 Returns **exact video timestamps**
- 📊 Relevance scoring (High / Medium / Low)
- 🎥 Designed for **video-based learning**
- ⚡ Fast retrieval using precomputed embeddings

---

## 🧠 How It Works (RAG Pipeline)

1. User asks a question  
2. Query is converted into embedding  
3. Compared with stored embeddings using cosine similarity  
4. Top relevant video chunks are selected  
5. LLM generates a human-friendly response  
6. User is guided to exact video timestamps  

---

## 📁 Project Structure

```
RAG-BASED-AI/
│
├── jsons                 # Input subtitle chunks
├── embeddings.joblib     # Stored embeddings
├── merge_chunks.py       # Combine small chunks
├── preprocess_json.py    # JSON → embeddings
├── mp3_to_json.py        # Audio → JSON
├── video_to_mp3.py       # Video → MP3
├── process_incoming.py   # Main query pipeline
├── prompt.txt            # Generated prompt
├── response.txt          # LLM output
└── README.md