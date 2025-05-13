import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    'País': ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panamá'],
    'Exportaciones (USD millones)': [4291.2, 1416.4, 10450.0, 3440.0, 1780.0, 8768.0]
}

df = pd.DataFrame(data)

# Título del dashboard con emoji
st.title("📊 Dashboard de Exportaciones en Centroamérica")

# Mostrar tabla
st.dataframe(df)

# Gráfico de barras
fig, ax = plt.subplots()
ax.bar(df['País'], df['Exportaciones (USD millones)'], color=['#2E86C1', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8', '#EBF5FB'])
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title("Exportaciones en Centroamérica")
plt.xticks(rotation=45)
st.pyplot(fig)
