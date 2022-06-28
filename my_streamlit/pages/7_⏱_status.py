import streamlit as st
import time

# Page title
st.title("Status")
st.text("O Streamlit também fornece widgets para que consigamos comunicar status com a pessoa usuária")

# Progress Bar
st.header("Barra de progresso")
st.code('''
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
''')

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

# Spinner
st.header("Spinner")
st.code('''
with st.spinner("Aguarde um pouco ..."):
    time.sleep(10)
''')
with st.spinner("Aguarde um pouco ..."):
    time.sleep(10)

# Celebration
st.header("Celebrações")
st.text("Existem duas animações de celebração")
st.code('''
st.ballons()
st.snow()
''')
with st.spinner("Aguarde um pouco ..."):
    time.sleep(5)
st.balloons()
st.snow()

# Messages
st.header("Mensagens")
st.text("Também podemos criar caixas de mensagems para a pessoa usuária")
st.code('''
st.error("Essa é uma mensagem de erro")
st.warning("Esse é um aviso")
st.info("Essa é uma mensagem de informação")
st.success("Essa é uma mensagem de sucesso")
        ''')
st.error("Essa é uma mensagem de erro")
st.warning("Esse é um aviso")
st.info("Essa é uma mensagem de informação")
st.success("Essa é uma mensagem de sucesso")