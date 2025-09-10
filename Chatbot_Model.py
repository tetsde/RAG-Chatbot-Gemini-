import google.generativeai as genai
from Vector_Store import get_vectorstore, search
genai.configure(api_key="insert_your_api_key_here")
conversation_history = []
def rag_chatbot(query):
    global conversation_history
    
    index, documents, model = get_vectorstore()

    results = search(query, index, documents, model, k=3)
    context = "\n".join([
        f"{doc['title']}: {doc['content']}" if isinstance(doc, dict) else str(doc)
        for doc in results
    ])

    conversation_history.append({"role": "user", "content": query})

    history_text = "\n".join([
        f"Người dùng: {turn['content']}" if turn["role"] == "user" else f"Trợ lý: {turn['content']}"
        for turn in conversation_history[-5:]  # nhớ 5 lượt gần nhất
    ])

    prompt = f"""
    Bạn là một trợ lý thông minh, luôn nhớ hội thoại trước đó. 
    Đây là lịch sử hội thoại gần đây:
    {history_text}

    Dưới đây là thông tin tham chiếu:
    {context}

    Câu hỏi mới:
    {query}

    Trả lời bằng tiếng Việt, ngắn gọn và dễ hiểu.
    """

    model_gemini = genai.GenerativeModel("gemini-2.0-flash")
    response = model_gemini.generate_content(prompt)

    conversation_history.append({"role": "assistant", "content": response.text})

    return response.text


if __name__ == "__main__":
    while True:
        query = input(" User: ")
        if query.lower() in ["exit", "quit"]:
            print("Tạm biệt!")
            break

        answer = rag_chatbot(query)
        print("Gemini:", answer)
