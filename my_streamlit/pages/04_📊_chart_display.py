import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

def create_data(nrows):
    data = np.random.randn(nrows, 4)
    df = pd.DataFrame(data, columns=["A", "B", "C", "D"])
    return df

def create_data_lat_long(nrows):
    data = np.random.randn(nrows, 2)*0.1
    df = pd.DataFrame(data, columns=["latitude", "longitude"])
    df['latitude'] += -23.5
    df["longitude"] += -46.6
    return df

df = create_data(10)
df_lat_long = create_data_lat_long(100)
# Page title
st.title("Gráficos")

# Line chart
st.text("O Streamlit já vem com alguns tipos de gráficos implementados.")
st.text("Um deles é o gráfico de linhas.")
st.code("st.line_chart(df)")
st.line_chart(df)

# Bar chart
st.text("Também podemos criar um gráfico de barras")
st.code("st.bar_chart(df)")
st.bar_chart(df)

# Area chart
st.text("Ou um gráfico de área")
st.code("st.area_chart(df)")
st.area_chart(df)

# Other libs
st.markdown("Apesar de já termos alguns gráficos por parão, podemos usar algumas das libs mais comums como `matplotlib`, `bokeh` ou `plotly`")
fig, ax = plt.subplots()
ax.plot(range(10), df["A"])
st.pyplot(fig)

# Maps
st.text("Uma outra funcionalidade muito útil é a criação de mapas")
st.code("st.map(df_lat_long)")
st.map(df_lat_long)
