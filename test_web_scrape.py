from llama_index.readers.web import SimpleWebPageReader

# Danh sách URL cần lấy nội dung
urls = [
    "https://luyenthieps.vn/",
    "https://thithu.luyenthieps.vn/"
]

# Tải nội dung HTML và chuyển thành văn bản
documents = SimpleWebPageReader(html_to_text=True).load_data(urls)

# Hiển thị 500 ký tự đầu tiên từ mỗi trang
for i, doc in enumerate(documents):
    print(f"--- Trang {i+1} ---")
    print(doc.text[:500])
