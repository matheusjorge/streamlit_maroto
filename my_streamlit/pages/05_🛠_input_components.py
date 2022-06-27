import streamlit as st

# Page title
st.title("Componentes de entrada")

st.text("O Streamlit fornece vários tipos de componentes para pegar inputs das pessoas usuárias")

# Text input
st.header("Texto Aberto")
st.text("Temos dois elementos de texto aberto")

st.subheader("Text area")
st.code("st.text_area('Digite seu texto aqui')")
input1 = st.text_area('Digite seu texto aqui')
st.text(f"Você digitou '{input1}'")

st.subheader("Text input")
st.code("st.text_input('Digite seu texto aqui')")
input2 = st.text_input('Digite seu texto aqui')
st.text(f"Você digitou '{input2}'")

# Number inputs
st.header("Números")
st.text("Temos algumas opções para recer números")

st.subheader("Number input")
st.code("st.number_input('Escolha um número', min_value=0, max_value=10)")
number = st.number_input('Escolha um número', min_value=0, max_value=10)
st.text(f"Você escolheu o número '{number}'")

st.subheader("Slider")
st.code("st.slider('Escolha um número', min_value=0, max_value=10)")
slider = st.slider('Escolha um número', min_value=0, max_value=10)
st.text(f"Você escolheu o número '{slider}'")

# Selection components
st.header("Seleção")
st.text("Também existem alguns componentes de seleção")

st.subheader("Checkbox")
st.code("st.checkbox('Eu concordo')")
if st.checkbox("Eu concordo"):
    st.text("Você concorda!")
else:
    st.text("Você discorda!")

st.subheader("Radio Button")
st.code('st.radio("Escolha 1", ["Opção 1", "Opção 2", "Opção 3"])')
radio = st.radio("Escolha 1", ["Opção 1", "Opção 2", "Opção 3"])
st.text(f"Você escolheu '{radio}'")

st.subheader("Select Box")
st.code('st.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])')
select_box = st.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])
st.text(f"Você selecionou '{select_box}'")

st.subheader("Multi Select Box")
st.code('st.multiselect("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])')
multiselect = st.multiselect("Selecione as opções", ["Opção 1", "Opção 2", "Opção 3"])
st.text(f"Você selecionou '{multiselect}'")

st.subheader("Select Slider")
st.code('st.selectslider("Selecione uma opção", ["Pouco", "Médio", "Muito"])')
select_slider = st.select_slider("Selecione as opções", ["Pouco", "Médio", "Muito"])
st.text(f"Você selecionou '{select_slider}'")

# Buttons
st.header("Botões")
st.text("Existem também botões pré configurados")

st.subheader("Botão simples")
st.code('st.button("Clique aqui")')
button = st.button("Clique aqui")
if button:
    st.text("Você clicou")
else:
    st.text("Você não clicou")

st.subheader("Botão de Download")
st.code('st.download_button("Download", data="Parabéns! Você fez um download", file_name="seu_download.txt")')
st.download_button("Download", data="Parabéns! Você fez um download", file_name="seu_download.txt")

# Datetime
st.header("Datas")
st.text("Outra possibilidade é de escolher datas e horários.")
st.subheader("Seletor de Data")
st.code('st.date_input("Selecione a data de início")')
date = st.date_input("Selecione a data de início")
st.text(f"Você selecionou '{date}'")

st.subheader("Seletor de Horário")
st.code('st.time_input("Selecione o horário de início")')
time = st.time_input("Selecione a horário de início")
st.text(f"Você selecionou '{time}'")

# Color
st.header("Cores")
st.text("O streamlit também tem um selector de cores")
st.code('color = st.color_picker("Selecione a cor desejada")')
color = st.color_picker("Selecione a cor desejada")
st.markdown(f"A cor selecionada é<p style=color:{color}>{color}</p>", unsafe_allow_html=True)

# Media
st.header("Mídia")
st.text("Por fim, temos as entradas de mídia.")

st.subheader("Uploader de Arquivos")
st.code('st.file_uploader("Inclua sua imagem aqui", type=["png", "jpg", "jpeg"], accept_multiple_files=False)')
file = st.file_uploader("Inclua sua imagem aqui", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
st.write(file)

st.subheader("Câmera")
st.code('st.camera_input("Tire uma foto sua")')
camera = st.camera_input("Tire uma foto sua")
st.write(camera)
