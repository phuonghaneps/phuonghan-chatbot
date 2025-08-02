# ingest.py
import os, pickle
import faiss
from sentence_transformers import SentenceTransformer

DATA_FILE = "data/datasample.txt"
VECTOR_DIR = "logs/vector_store"

# Tạo thư mục lưu vector nếu chưa có
os.makedirs(VECTOR_DIR, exist_ok=True)

# Load dữ liệu
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    texts = [line.strip() for line in f if line.strip()]

# Khởi tạo model embedding
model = SentenceTransformer('distiluse-base-multilingual-cased-v1')
embeddings = model.encode(texts)

# Tạo FAISS index và lưu lại
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, f"{VECTOR_DIR}/faiss_index.idx")

# Lưu lại dữ liệu gốc
with open(f"{VECTOR_DIR}/texts.pkl", "wb") as f:
    pickle.dump(texts, f)

print("✅ Đã nạp dữ liệu và tạo vector thành công.")
