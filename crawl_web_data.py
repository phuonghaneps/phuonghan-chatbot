from llama_index.readers.web import SimpleWebPageReader

# Danh sách URL từ website của bạn
urls = [
    "https://luyenthieps.vn/",
    "https://thithu.luyenthieps.vn/"
]

# Trích xuất nội dung từ các trang web
documents = SimpleWebPageReader(html_to_text=True).load_data(urls)

# Lưu nội dung vào file .txt
with open("web_data.txt", "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc.text + "\n\n")

print("✅ Đã trích xuất và lưu dữ liệu web vào file web_data.txt")
