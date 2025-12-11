import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
# OpenAI Kütüphaneleri
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os

# Sayfa Ayarları
st.set_page_config(page_title="ChatGPT PDF Asistanı", page_icon="🤖")

st.markdown('<h1 style="text-align:center;">🤖 ChatGPT ile PDF Sohbeti</h1>', unsafe_allow_html=True)
st.write("Altyapı: OpenAI GPT-3.5 Turbo")

# Sidebar
with st.sidebar:
    st.title("Ayarlar")
    # OpenAI Key "sk-" ile başlar
    openai_api_key = st.text_input("OpenAI API Key:", type="password")
    st.markdown("[🔑 Key Almak İçin Tıkla](https://platform.openai.com/api-keys)")
    st.markdown("---")
    uploaded_file = st.file_uploader("Bir PDF Dosyası Yükle", type="pdf")

# Ana Akış
if uploaded_file and openai_api_key:
    # 1. PDF Okuma
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    
    st.success(f"✅ Dosya okundu! ({len(text)} karakter)")
    
    # 2. Metni Bölme
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # 3. Embedding (OpenAI Kullanarak)
    try:
        with st.spinner("Veritabanı hazırlanıyor (OpenAI)..."):
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        
        st.success("🚀 Hazır! Sorunu bekliyorum.")

        # 4. Soru-Cevap
        query = st.text_input("Doküman hakkında ne bilmek istersin?")
        
        if query:
            docs = vector_store.similarity_search(query=query, k=3)
            
            # --- MODEL: GPT-3.5 Turbo ---
            llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
            # ----------------------------
            
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            
            with st.spinner("ChatGPT düşünüyor..."):
                response = chain.run(input_documents=docs, question=query)
                
            st.markdown("### 🤖 Cevap:")
            st.write(response)
            
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
        st.info("İpucu: OpenAI hesabında kredi olduğundan veya deneme süresinin bitmediğinden emin ol.")

elif not openai_api_key:
    st.warning("👈 Soldaki menüden OpenAI API Key ('sk-' ile başlayan) gir.")
else:
    st.info("👈 Başlamak için PDF yükle.")