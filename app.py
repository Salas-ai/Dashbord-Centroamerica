import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
# Datos de exportaciones
data_exportaciones = {
    'País': ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Panamá'],
    'Exportaciones (USD millones)': [4291.2, 1416.4, 10450.0, 3440.0, 8768.0]
}
df_exportaciones = pd.DataFrame(data_exportaciones)

# Datos de segmentos de clientes
data_segmentos = {
    'País': ['Estados Unidos', 'México', 'Colombia', 'Brasil', 'Argentina'],
    'Segmento de Clientes': ['Hospitales', 'Clínicas', 'Consultorios', 'Gobiernos', 'Distribuidores'],
    'Tamaño del Mercado (USD millones)': [5000, 1500, 1200, 3000, 700]
}
df_segmentos = pd.DataFrame(data_segmentos)

# Título del dashboard con emoji
st.title("📊 Dashboard de Exportaciones y Segmentos de Clientes en Centroamérica")

# Mostrar tabla de exportaciones
st.subheader("Exportaciones de Dispositivos Médicos")
st.dataframe(df_exportaciones)

# Gráfico de barras de exportaciones
fig, ax = plt.subplots()
ax.bar(df_exportaciones['País'], df_exportaciones['Exportaciones (USD millones)'], color=['#2E86C1', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8'])
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title("Exportaciones en Centroamérica")
plt.xticks(rotation=45)
st.pyplot(fig)

# Mostrar tabla de segmentos de clientes
st.subheader("Segmentos de Clientes y Tamaño del Mercado")
st.dataframe(df_segmentos)

# Gráfico de barras de segmentos de clientes
fig2, ax2 = plt.subplots()
ax2.bar(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)'], color=['#FF6347', '#FFB6C1', '#98FB98', '#FFD700', '#40E0D0'])
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Tamaño del Mercado por Segmento de Clientes")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Análisis y decisión de explorar nuevos mercados
st.subheader("Criterios para Expandir o Mantener Mercados")

# Añadir lógica para determinar si explorar nuevos mercados o mantener los actuales
# Aquí puedes usar una simple regla para determinar si explorar un mercado, por ejemplo:
for country in df_segmentos['País']:
    market_size = df_segmentos[df_segmentos['País'] == country]['Tamaño del Mercado (USD millones)'].values[0]
    if market_size < 2000:
        decision = "Explorar Nuevos Mercados"
    else:
        decision = "Mantener Mercado Actual"
    st.write(f"En {country}, el mercado de dispositivos médicos tiene un tamaño de {market_size} millones USD: {decision}")

