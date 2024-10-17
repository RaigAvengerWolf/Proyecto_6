import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lee los datos del archivo vehicles

# esta linea crea una casilla de verificacion para el histograma
show_hist = st.checkbox('Mostrar histograma') 

# esta linea crea una casilla de verificacion para grafico
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Si se selecciona la casilla para el histograma
if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crea un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Muestra el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Si se selecciona la casilla para el gráfico 
if show_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs. kilometraje')
    # Crea el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje")
    # Muestra el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)