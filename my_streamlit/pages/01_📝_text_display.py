import streamlit as st

# Title
st.write("Nós podemos adicionar um título a nossa página com")
st.code("st.title('Título da página')")
st.write("e ele ficaria assim: ")
st.title("Título da página")

# Header
st.text("Nós também podemos adicionar cabeçalhos e subcabeçalhos para nos ajudar a organizar melhor os conteúdo")
st.code("""
st.header("Este é um cabeçalho")
st.subheader("Este é um sub cabeçalho")
        """)
st.header("Este é um cabeçalho")
st.subheader("Este é um sub cabeçalho")

# Caption
st.text("E se quisermos adicionar uma legenda depois de algum elemento? Também é possível!")
st.code("st.caption('Código para gerar legenda')")
st.caption('Código para gerar legenda')

# Latex
st.text("Um outra funcionalidade muito legal é que conseguimos mostrar equações usando LaTeX!")
st.code(r"st.latex('MSE = \frac{1}{n} \sum (y - \hat{y})^2')")
st.latex(r"MSE = \frac{1}{n} \sum (y - \hat{y})^2")

# Markdown
st.text("Também podemos personalizar nossos textos utilizam a sintaxe de markdown!")
st.markdown("**este texto está em negrito**")
st.markdown("*este está em itálico*")
st.markdown("""
eu consigo criar uma lista:
- item 1
- item 2

e uma lista numerada
1. Item 1
2. Item 2
""")

