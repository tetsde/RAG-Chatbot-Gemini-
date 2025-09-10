import google.generativeai as genai
from Vector_Store import get_vectorstore, search
genai.configure(api_key="insert_your_api_key_here")
conversation_history = []
def rag_chatbot(query):
    global conversation_history
    
    index, documents, model = get_vectorstore()

    results = search(query, index, documents, model, k=15)
    context = "\n".join([
    f"{doc.get('original_item', {}).get('title', 'Không có tiêu đề')}: {doc.get('original_item', {}).get('content', doc.get('chunk_text', ''))}"
    if isinstance(doc, dict) else str(doc)
    for doc in results
])

    conversation_history.append({"role": "user", "content": query})

    history_text = "\n".join([
        f"Người dùng: {turn['content']}" if turn["role"] == "user" else f"Trợ lý: {turn['content']}"
        for turn in conversation_history[-5:]  # nhớ 5 lượt gần nhất
    ])

    prompt = f"""
Task: Trả lời câu hỏi mới từ người dùng dựa trên dữ liệu tham chiếu và lịch sử hội thoại gần đây, đảm bảo thông tin chính xác, đầy đủ, logic và liên quan trực tiếp.

Context: 
1. Lịch sử hội thoại gần đây giữa người dùng và trợ lý: {history_text}
2. Thông tin tham chiếu có thể hữu ích để trả lời câu hỏi: {context}

Role: Bạn là một trợ lý thông minh, luôn nhớ hội thoại trước đó, có khả năng phân tích, tổng hợp dữ liệu từ nhiều nguồn, lọc ra thông tin quan trọng và trả lời súc tích, dễ hiểu.

Example: 
- Nếu câu hỏi là “X là gì?”, hãy trả lời giải thích chi tiết, kèm ví dụ minh họa và dẫn chứng từ thông tin tham chiếu khi có.
- Nếu thông tin tham chiếu mâu thuẫn, hãy tổng hợp và nêu rõ nguồn hoặc ghi chú sự khác nhau.

Instruction: 
1. Đọc kỹ thông tin tham chiếu, tóm tắt các điểm quan trọng liên quan đến câu hỏi.
2. Trả lời câu hỏi: {query}
3. Trả lời bằng tiếng Việt, rõ ràng, đầy đủ thông tin, logic, có dẫn chứng nếu cần.
4. Nếu không chắc chắn thông tin, hãy ghi chú rằng câu trả lời dựa trên dữ liệu tham chiếu hiện có.
"""

    model_gemini = genai.GenerativeModel("gemini-2.0-flash")
    response = model_gemini.generate_content(prompt)

    conversation_history.append({"role": "assistant", "content": response.text})

    return response.text


if __name__ == "__main__":
    while True:
        query = input("User: ")
        if query.lower() in ["exit", "quit"]:
            print("Tạm biệt!")
            break

        answer = rag_chatbot(query)
        print("Gemini:", answer)
