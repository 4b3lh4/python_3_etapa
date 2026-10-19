import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu primeiro dash", page_icon="🛒", layout="centered")

nome = "Alice"
idade = 17

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.write("Olá, mundo!")

st.title("Meu primeiro dash")
st.write("Nome:", nome)
st.write("Idade:", idade)
st.dataframe(df)

st.header("Supermercado")

produtos = {
    "Arroz": 25.00,
    "Feijão": 8.00,
    "Leite": 5.00,
    "Pão": 10.00,
    "Café": 18.50,
    "Açúcar": 4.50
}


def calcular_total(selecionados):
    total = 0
    for produto in selecionados:
        total = total + produtos[produto]
    return total


col1, col2 = st.columns(2)

with col1:
    selecionados = st.multiselect("Escolha os produtos:", list(produtos.keys()))

total = calcular_total(selecionados)

with col2:
    valor_pago = st.number_input("Valor pago em dinheiro (R$):", min_value=0.0, step=1.0, format="%.2f")

st.write(f"Total da compra: R$ {total:.2f}")

if st.button("Calcular troco"):
    if len(selecionados) == 0:
        st.error("Selecione pelo menos um produto.")
    elif valor_pago < total:
        st.error(f"Valor insuficiente! Faltam R$ {total - valor_pago:.2f}")
    else:
        troco = valor_pago - total
        st.success(f"Pagamento aprovado! Troco: R$ {troco:.2f}")
