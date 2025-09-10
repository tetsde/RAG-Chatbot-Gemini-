# RAG Chatbot with Google Gemini

This project builds a **Retrieval-Augmented Generation (RAG) chatbot** using **Google Gemini API** and **Vector Database (FAISS)**.  

The chatbot can:
- Retrieve internal data from the vector store.  
- Integrate with **Gemini** to generate natural responses.  
- **Memory**: remember recent conversations to provide coherent replies.  

---

## ✨ Key Features
- **RAG System**: search for information from pre-embedded documents.  
- **Gemini Integration**: powered by Google’s `gemini-2.0-flash` model.  
- **Conversation Memory**: the chatbot remembers the last 5 turns of dialogue.  
- **CLI Mode**: run directly in the terminal.  

---

## 📂 Sample Dataset
The system is currently running with **sample internal company data**, including:  
- **Company progress reports** (monthly, quarterly, yearly).  
- **Employee work schedules**.  
- **Ongoing projects** by departments.  

**Goal**: help the director easily monitor company performance and quickly access internal information.  

Example of a sample record:
```json
{
  "id": "1",
  "category": "Tiến độ công ty",
  "title": "Báo cáo tiến độ số 1",
  "content": "Báo cáo tiến độ công ty tháng 1/2025: Hoàn thành 71% mục tiêu. Doanh thu tăng 6% so với tháng trước."
}
