import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('./vehicles_us.csv')
st.header('Características de los carros en anuncios de venta ')
st.dataframe(car_data)

hist_button = st.button('Construir histograma')
scat_button = st.button('Construir un gráfico de dispersión')
histo_button = st.button('Construir un histograma de la condición') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el odómetro de coches en anuncio')
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    st.write('Creación de un gráfico de dispersión relación odómetro - precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True) 

if histo_button:
    st.write('Creación de histograma de la condición de acuerdo al año del carro')
    fig = px.histogram(car_data, x="model_year", color = 'condition')
    st.plotly_chart(fig, use_container_width=True) 
