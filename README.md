#  RAG Chatbot with Google Gemini

Dự án này xây dựng một **chatbot RAG (Retrieval-Augmented Generation)** sử dụng **Google Gemini API** và **Vector Database (FAISS)**.  
Chatbot có khả năng:
- Truy xuất dữ liệu nội bộ từ vector store.
- Tích hợp với **Gemini** để tạo câu trả lời tự nhiên.
- **Memory**: ghi nhớ hội thoại gần đây để phản hồi mạch lạc, không rời rạc.

---

##  Tính năng chính
- **RAG System**: tìm kiếm thông tin từ tài liệu đã được embedding.
- **Gemini Integration**: sử dụng model `gemini-2.0-flash` của Google.
- **Conversation Memory**: chatbot nhớ 5 lượt hội thoại gần nhất.
- **CLI Mode**: chạy trực tiếp trên terminal.

---

## Dataset mẫu
Hệ thống hiện đang chạy với **mẫu dữ liệu nội bộ công ty**, bao gồm:
- **Tiến độ làm việc của công ty** (theo tháng, quý, năm).
- **Lịch làm việc của nhân sự**.
- **Các dự án đang dang dở** của từng phòng ban.  

Mục tiêu: hỗ trợ giám đốc dễ dàng kiểm soát tình hình công ty và truy xuất nhanh thông tin nội bộ.

Ví dụ một mẫu dữ liệu:
```json
{
  "id": "1",
  "category": "Tiến độ công ty",
  "title": "Báo cáo tiến độ số 1",
  "content": "Báo cáo tiến độ công ty tháng 1/2025: Hoàn thành 71% mục tiêu. Doanh thu tăng 6% so với tháng trước."
}
