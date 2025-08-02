# main.py

from transformers import pipeline
from gtts import gTTS
from langdetect import detect
import faiss
import pickle
import uuid
import os
from sentence_transformers import SentenceTransformer


def load_vector_store():
    VECTOR_FOLDER = 'logs/vector_store'
    try:
        index = faiss.read_index(f'{VECTOR_FOLDER}/faiss_index.idx')
        with open(f'{VECTOR_FOLDER}/texts.pkl', 'rb') as f:
            texts = pickle.load(f)
        return index, texts
    except Exception as e:
        print(f"❌ Không thể tải FAISS index hoặc dữ liệu: {e}")
        input("→ Nhấn Enter để thoát...")
        exit()


def speak(text):
    try:
        lang = detect(text)
    except:
        lang = 'vi'
    tts = gTTS(text, lang='vi' if lang == 'vi' else 'en')
    filename = f"voice_{uuid.uuid4().hex[:8]}.mp3"
    tts.save(filename)
    os.system(f'start {filename}')


def main():
    print("🔁 Đang tải mô hình AI PHEPSChatAI...")

    index, texts = load_vector_store()

    embedder = SentenceTransformer('distiluse-base-multilingual-cased-v1')
    generator = pipeline("text-generation", model="VietAI/gpt-neo-1.3B-vietnamese-news")

    print("\n🤖 PHEPSChatAI đã sẵn sàng! (gõ 'exit' để thoát)\n")

    while True:
        try:
            query = input("👤 Bạn: ").strip()
            if query.lower() == "exit":
                print("👋 Tạm biệt!")
                break

            if not query:
                continue

            # Vector hóa và tìm context phù hợp
            vec = embedder.encode([query])
            D, I = index.search(vec, k=1)
            context = texts[I[0][0]]

            # Tạo prompt kết hợp
            prompt = f"{context}\nCâu hỏi: {query}\nTrả lời:"
            output = generator(prompt, max_length=200)[0]["generated_text"]
            response = output[len(prompt):].strip()

            print(f"🤖 AI: {response}")
            speak(response)

        except KeyboardInterrupt:
            print("\n🛑 Đã thoát chatbot.")
            break
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            continue


if __name__ == "__main__":
    main()
