<img width="1510" height="573" alt="image" src="https://github.com/user-attachments/assets/8f8b27bc-5d60-427f-8f85-cf5fb2e3ca6a" /># 🤖 Chat with PDF (RAG Pipeline)

An interactive AI-powered application that allows users to "chat" with their PDF documents. Built with **Streamlit**, **LangChain**, and **OpenAI**, this tool utilizes Retrieval-Augmented Generation (RAG) to provide accurate answers based on the document's content.

## 🚀 Features

* **Interactive Chat Interface:** Natural language Q&A with your documents.
* **RAG Architecture:** Uses FAISS vector store for efficient similarity search.
* **Secure:** API keys are handled securely within the session.
* **Instant Analysis:** Upload a PDF and start asking questions in seconds.
* **Model:** Powered by OpenAI's GPT-3.5 Turbo.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit:** For the frontend user interface.
* **LangChain:** For orchestration and chain management.
* **OpenAI API:** For embeddings and language processing.
* **FAISS:** For vector storage and retrieval.

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/chat-with-pdf.git](https://github.com/KULLANICI_ADIN/chat-with-pdf.git)
    cd chat-with-pdf
    ```

2.  **Create a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

##  Usage

1.  Enter your **OpenAI API Key** in the sidebar (starts with `sk-`).
2.  Upload a **PDF document**.
3.  Ask a question about the document in the chat box!

---
*Developed by BaramPolat*
