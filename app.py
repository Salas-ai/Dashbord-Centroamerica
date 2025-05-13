import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de Segmentos de Clientes
data_segmentos = {
    'País': ['Estados Unidos', 'México', 'Colombia', 'Brasil', 'Argentina'],
    'Segmento de Clientes': ['Hospitales', 'Clínicas', 'Consultorios', 'Gobiernos', 'Distribuidores'],
    'Tamaño del Mercado (USD millones)': [5000, 1500, 1200, 3000, 700]
}

df_segmentos = pd.DataFrame(data_segmentos)

# Datos de Empresas
data_empresas = {
    'Empresa': ['Meditech', 'BioMed', 'HealthPro', 'MediDevices', 'GlobalHealth'],
    'País': ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Panamá'],
    'Productos': ['Dispositivos Médicos', 'Equipos de Diagnóstico', 'Monitores de Pacientes', 'Sistemas de Esterilización', 'Sillas de Ruedas'],
    'Relevancia': [95, 87, 80, 65, 90]
}

df_empresas = pd.DataFrame(data_empresas)

# Datos de Exportaciones
data_exportaciones = {
    'País': ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Panamá'],
    'Exportaciones (USD millones)': [4291.2, 1416.4, 10450.0, 3440.0, 8768.0]
}

df_exportaciones = pd.DataFrame(data_exportaciones)

# Título del dashboard con emoji
st.title("📊 Dashboard de Exportaciones y Empresas en Centroamérica")

# Mostrar tabla de segmentos de clientes
st.subheader("Segmentos de Clientes por País")
st.dataframe(df_segmentos)

# Gráfico de barras de Segmentos de Clientes
fig_segmentos, ax_segmentos = plt.subplots()
ax_segmentos.bar(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)'], color=['#2E86C1', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8'])
ax_segmentos.set_xlabel("País")
ax_segmentos.set_ylabel("Tamaño del Mercado (USD millones)")
ax_segmentos.set_title("Tamaño del Mercado por País")
plt.xticks(rotation=45)
st.pyplot(fig_segmentos)

# Mostrar tabla de empresas
st.subheader("Empresas en Centroamérica")
st.dataframe(df_empresas)

# Gráfico de barras de Relevancia de Empresas
fig_empresas, ax_empresas = plt.subplots()
ax_empresas.bar(df_empresas['Empresa'], df_empresas['Relevancia'], color=['#2E86C1', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8'])
ax_empresas.set_xlabel("Empresa")
ax_empresas.set_ylabel("Relevancia (%)")
ax_empresas.set_title("Relevancia de Empresas en Dispositivos Médicos")
plt.xticks(rotation=45)
st.pyplot(fig_empresas)

# Mostrar tabla de exportaciones
st.subheader("Exportaciones de Dispositivos Médicos por País")
st.dataframe(df_exportaciones)

# Gráfico de barras de Exportaciones por País
fig_exportaciones, ax_exportaciones = plt.subplots()
ax_exportaciones.bar(df_exportaciones['País'], df_exportaciones['Exportaciones (USD millones)'], color=['#2ECC71', '#F39C12', '#9B59B6', '#34495E', '#1ABC9C'])
ax_exportaciones.set_xlabel("País")
ax_exportaciones.set_ylabel("Exportaciones (USD millones)")
ax_exportaciones.set_title("Exportaciones de Dispositivos Médicos por País")
plt.xticks(rotation=45)
st.pyplot(fig_exportaciones)

# Criterios de Decisión Estratégica

# Comparar los mercados actuales con los mercados potenciales
st.subheader("🌎 Criterios para Expandir o Mantener Mercados")
for index, row in df_exportaciones.iterrows():
    current_market = row['Exportaciones (USD millones)']
    country = row['País']
    potential_market = df_segmentos.loc[df_segmentos['País'] == country, 'Tamaño del Mercado (USD millones)'].values[0]

    # Decisión
    if potential_market > current_market:
        st.write(f"🌍 **Explorar nuevo mercado en {country}**: El mercado potencial ({potential_market} USD) es mayor que el actual ({current_market} USD).")
    else:
        st.write(f"✅ **Mantener mercado en {country}**: El mercado actual ({current_market} USD) es suficiente para mantener la relevancia.")
