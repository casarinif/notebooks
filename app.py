import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura do conjunto de dados
car_data = pd.read_csv('vehicles_us.csv')

# Função para gerar histograma
def gerar_histograma():
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Função para gerar gráfico de dispersão
def gerar_grafico_dispersao():
    st.write('Criando um gráfico de dispersão entre odometer e price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Botões para gerar gráficos
hist_button = st.button('Criar Histograma')
scatter_button = st.button('Criar Gráfico de Dispersão')

# Gera o gráfico selecionado
if hist_button:
    gerar_histograma()
elif scatter_button:
    gerar_grafico_dispersao()

# Opcional: Caixas de seleção
build_histogram = st.checkbox('Criar um Histograma')
build_scatter = st.checkbox('Criar um Gráfico de Dispersão')

# Gera o gráfico de acordo com a caixa de seleção
if build_histogram:
    gerar_histograma()
elif build_scatter:
    gerar_grafico_dispersao()
