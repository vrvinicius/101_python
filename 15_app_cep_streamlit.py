import streamlit as st
import requests
import pandas as pd

st.title("Busca CEP")

cep = st.text_input("Busque seu CEP: ")

url = "https://viacep.com.br/ws/{cep}/json/"

if cep != "":

    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index=True)

    except Exception as err:
        st.error("Entre com um CEP válido!")