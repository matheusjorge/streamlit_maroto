import streamlit as st
import time

init = time.time()
# Page title
st.title("Performance")
st.text("Muitas vezes, no nosso fluxo de execução, temos alguma etapa que demora muito e só precisamos executá-la uma vez.")
st.text("Nesses casos, podemos usar a função de cache do Streamlit para nos ajudar")

@st.cache
def funcao_demorada():
    time.sleep(10)

funcao_demorada()

st.text(f"Tempo de execução: {time.time() - init}")