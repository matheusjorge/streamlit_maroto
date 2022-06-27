import streamlit as st
import time


# Page title
st.title("Layouts")

# Sidebar
st.header("Barra Lateral")
st.text("Podemos incluir os mesmos widgets que acabamos de ver, na barra lateral.")
st.code('st.sidebar.radio("Selecione uma opção", ["Opção 1", "Opção 2"])')
radio = st.sidebar.radio("Selecione uma opção", ["Opção 1", "Opção 2"])
st.text(f"Você selecionou {radio}")

# Coluns
st.header("Colunas")
st.text("Uma opção para melhorar o layout é a criação de colunas")
st.code('''
cols = st.columns(3)
for i, col in enumerate(cols):
    with col:
        st.text(f"eu sou a coluna {i}")''')
cols = st.columns(3)
for i, col in enumerate(cols):
    with col:
        st.text(f"eu sou a coluna {i}")

# Expanders
st.header("Expansores")
st.text("Uma outra forma de organizar seções é por meio dos expansores")
st.code('''
with st.expander("Clique para saber mais"):
    st.text("Alguma informação útil!")
        ''')
with st.expander("Clique para saber mais"):
    st.text("Alguma informação útil!")

# Empty
st.header("Empty (Vazio)")
st.text("Podemos usar a funcionalidade de empty do Streamlit para sobrescrevermos o mesmo \nobjeto")
with st.empty():
    for seconds in range(30):
        st.write(f"⏳ {seconds} segundos se passaram")
        time.sleep(1)
    st.write("✔️ 30 segundos acabaram!")
