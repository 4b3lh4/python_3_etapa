import streamlit as st
import pandas as pd

nome = "Seu Nome"
idade = 20

st.write("Olá, mundo")
st.write(f"Meu nome é {nome} e tenho {idade} anos")

st.title("Meu primeiro dash")
st.subheader(nome)

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.write(df)

st.divider()

precos = {
    "Arroz": 28.90,
    "Feijão": 8.50,
    "Macarrão": 5.20,
    "Leite": 5.80,
    "Café": 18.90,
    "Pão": 9.50
}


def calcular_compra(item, quantidade):
    return precos[item] * quantidade


st.subheader("Supermercado")

item = st.selectbox("Escolha um item", list(precos.keys()))
quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)

total = calcular_compra(item, quantidade)

st.metric("Total da compra", f"R$ {total:.2f}")