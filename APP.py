import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
st.header('Anunciamos la venta de tu coche')


def tipo():
    datos = pd.read_csv("vehicles_us.csv")

    boton_histograma = st.button(
        'Construir histograma de barras Tipos de vehiculos ')

    if boton_histograma:
        figura_type = px.histogram(datos, "type", title="Tipos de vehiculos")
        st.plotly_chart(figura_type)
        figura_type.show()


def km_valor():
    datos = pd.read_csv("vehicles_us.csv")

    boton_dispersion = st.button(
        'Construir gráfico de dispersión de km recorridos vs precio')

    if boton_dispersion:
        fig_hist = px.scatter(datos, "odometer", "price",
                              title="Gráfico de dispersión de km recorridos vs precio")
        st.plotly_chart(fig_hist)
        fig_hist.show()


def modelo():
    datos = pd.read_csv("vehicles_us.csv")

    build_barras = st.checkbox('Construir diagrama de barras')

    if build_barras:
        st.write(
            'Creación de un diagrama de barras de los Modelos vs los precio de vehiculos')
        figura_modelo = px.bar(datos, x="model", y="price",
                               title="Modelos vs precio de vehiculos")
        st.plotly_chart(figura_modelo)
        figura_modelo.show()


tipo()
km_valor()
modelo()
