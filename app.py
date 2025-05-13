import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    'País': ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panamá'],
    'Exportaciones (USD millones)': [4291.2, 1416.4, 10450.0, 3440.0, 1780.0, 8768.0]
}

df = pd.DataFrame(data)

# Título del dashboard
st.title("📊 Dashboard de Exportaciones en Centroamérica")

# Mostrar datos
st.dataframe(df)

# Gráfico de barras
st.bar_chart(df.set_index('País'))
