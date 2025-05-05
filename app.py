import streamlit as st
from datetime import datetime

# Dummy AI Response Function
def get_ai_recommendation(user, language, input_text):
    if language == "Indonesia":
        return f"Halo {user}, berikut rekomendasi belajarmu: Ringkasan topik '{input_text}', latihan soal, dan jadwal belajar selama 3 hari ke depan."
    else:
        return f"Hi {user}, here’s your learning recommendation: Summary of '{input_text}', practice questions, and a 3-day study plan."

# Title
st.set_page_config(page_title="AI Learning Assistant", layout="centered")
st.title("📚 AI Learning Assistant for Family")

# Select user
user = st.selectbox("Pilih Pengguna:", ["Ayah", "Ibu", "Anak"])

# Language selection
language = st.radio("Bahasa yang digunakan:", ["Indonesia", "English"])

# Learning topic input
st.subheader("Masukkan topik atau pertanyaan belajar:")
input_text = st.text_input("Contoh: Sistem pernapasan manusia atau What is photosynthesis?")

# File uploader
st.subheader("Upload tugas belajar (opsional):")
uploaded_file = st.file_uploader("Pilih file tugas (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

# Submit button
if st.button("🎯 Dapatkan Rekomendasi AI"):
    if input_text:
        recommendation = get_ai_recommendation(user, language, input_text)
        st.success("✅ Rekomendasi Belajar:")
        st.markdown(recommendation)
        
        if uploaded_file:
            st.info(f"📎 File '{uploaded_file.name}' berhasil diunggah. Akan diproses oleh AI pada versi berikutnya.")
    else:
        st.warning("Silakan masukkan topik belajar terlebih dahulu.")

# Footer
st.markdown("---")
st.caption("🚀 Dibuat dengan ❤️ oleh Ogenkz | Versi MVP")
