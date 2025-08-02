from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader
import os

# Danh sách URL bạn muốn trích xuất dữ liệu
urls = [
    "https://luyenthieps.vn/",
    "https://thithu.luyenthieps.vn/"
]

# Trích xuất nội dung từ web
documents = SimpleWebPageReader(html_to_text=True).load_data(urls)

# Tạo vector index
index = VectorStoreIndex.from_documents(documents)

# Lưu index lại để dùng sau
index.storage_context.persist(persist_dir="./web_index")
print("✅ Đã xây dựng xong index và lưu vào thư mục 'web_index'")
