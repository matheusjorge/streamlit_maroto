import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import streamlit as st

@st.cache
def load_iris_df():
    iris = load_iris()
    data = pd.DataFrame(iris["data"], columns=iris["feature_names"])
    data["target"] = iris["target"]
    data["target"].replace({i: c for i, c in enumerate(iris["target_names"])}, inplace=True)
    return data
data = load_iris_df()
def train_model(data):
    lr = LogisticRegression(max_iter=10_000)
    lr.fit(data.drop(columns="target").values, data["target"])
    return lr

model = train_model(data)

# Page title
st.title("Classificador - Iris")

st.header("Dados")
st.write(data)

st.header("Visualização")
cols = st.columns(2)
with cols[0]:
    xaxis = st.selectbox("Selecione o eixo X", data.drop(columns="target").columns)
with cols[1]:
    yaxis = st.selectbox("Selecione o eixo Y", data.drop(columns="target").columns)

fig, ax = plt.subplots(figsize=(16,9))
sns.scatterplot(data=data, x=xaxis, y=yaxis, hue="target", ax=ax)
st.pyplot(fig)

st.header("Predição")
petal_columns = st.columns(2)
sepal_columns = st.columns(2)

with petal_columns[0]:
    petal_width = st.slider(
        "petal_width",
        min_value=float(0.8*data["petal width (cm)"].min()),
        max_value=float(1.2*data["petal width (cm)"].max()),
        value=float(data["petal width (cm)"].mean())
    )

with petal_columns[1]:
    petal_length = st.slider(
        "petal_length",
        min_value=float(0.8*data["petal length (cm)"].min()),
        max_value=float(1.2*data["petal length (cm)"].max()),
        value=float(data["petal length (cm)"].mean())
    )

with sepal_columns[0]:
    sepal_width = st.slider(
        "sepal_width",
        min_value=float(0.8*data["sepal width (cm)"].min()),
        max_value=float(1.2*data["sepal width (cm)"].max()),
        value=float(data["sepal width (cm)"].mean())
    )

with sepal_columns[1]:
    sepal_length = st.slider(
        "sepal_length",
        min_value=float(0.8*data["sepal length (cm)"].min()),
        max_value=float(1.2*data["sepal length (cm)"].max()),
        value=float(data["sepal length (cm)"].mean())
    )

pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
st.markdown(f"Essa flor é da classe **{pred[0]}**")