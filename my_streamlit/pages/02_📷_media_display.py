import streamlit as st

# Page title
st.title("Elementos de mídia")

# Imagens
st.text("O streamlit permite que mostremos imagens de uma maneira super simples")
st.code("st.image('data/hans_ott.jpeg', caption='Essa é uma imagem fofa', width=400)")
st.image("data/hans_ott.jpeg", caption="Essa é uma imagem fofa", width=400)

# Video
st.text("Além de imagens, também podemos carregar vídeos")
st.code("st.video('https://www.youtube.com/watch?v=9wCnvr7Xw4E')")
st.video('https://www.youtube.com/watch?v=9wCnvr7Xw4E')

# Audio
st.text("E arquivos de áudio")
st.code("st.audio('data/81526__johnlavine333__hok.wav1')")
st.audio("data/81526__johnlavine333__hok.wav")