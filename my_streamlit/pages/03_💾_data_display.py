import numpy as np
import pandas as pd
import streamlit as st

def create_data(nrows):
    data = np.random.randn(nrows, 4)
    df = pd.DataFrame(data, columns=["A", "B", "C", "D"])
    return df

df = create_data(10)

# Page Title
st.title("Dados")

# Dinamic table
st.text("Existem dois modos de mostrar tabelas no Streamlit")
st.text("Podemos criar tabelas dinâmicas")
st.code("st.dataframe(df)")
st.dataframe(df)

# Static Tables
st.text("Ou podemos criar tabelas estáticas")
st.code("st.table(df)")
st.table(df)

# Json
st.text("Também podemos mostrar um DataFrame em formato Json")
st.code("st.json(df.to_json())")
st.json(df.to_json())

# Metrics
st.text("Uma funcionalidade muito legal é de mostrar métricas!")
st.code("""
st.metric(label="Acurácia", value="90%", delta="5%")
st.metric(label="Acurácia", value="90%", delta="-5%")
""")
st.metric(label="Acurácia", value="90%", delta="5%")
st.metric(label="Acurácia", value="90%", delta="-5%")