import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Función para obtener datos de exportaciones de dispositivos médicos desde la API UN COMTRADE
def get_export_data():
    url = 'https://comtradeapi.un.org/public/v1/preview'
    params = {
        'typeCode': 'C',  # Tipo de comercio (exportaciones)
        'reporterCode': '842',  # Código para Estados Unidos
        'partnerCode': '0',  # '0' significa todos los países
        'productCode': '9018',  # Código de productos de dispositivos médicos
        'startDate': '2010',
        'endDate': '2021',
        'frequencyCode': 'A',  # Datos anuales
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'data' in data:
        df = pd.json_normalize(data['data'])
        return df
    else:
        st.error("No se pudieron obtener los datos de exportaciones.")
        return pd.DataFrame()

# Cargar los datos desde la API
df_exportaciones_api = get_export_data()

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

# Título del dashboard con emoji
st.title("📊 Dashboard de Exportaciones y Empresas en Centroamérica")

# Mostrar la tabla de exportaciones desde API
st.subheader("Exportaciones de Dispositivos Médicos (Datos desde API)")
if not df_exportaciones_api.empty:
    st.dataframe(df_exportaciones_api)

# Gráfico de barras con las exportaciones
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_exportaciones_api['reporterLabel'], df_exportaciones_api['TradeValue'], color=['#2E86C1', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8'])
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title("Exportaciones de Dispositivos Médicos en Centroamérica desde API")
plt.xticks(rotation=45)
st.pyplot(fig)

# Mostrar tabla de segmentos de clientes
st.subheader("Segmentos de Clientes y Tamaño del Mercado")
st.dataframe(df_segmentos)

# Gráfico de tamaño de mercado
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)'], color=['#F39C12', '#F1C40F', '#E67E22', '#D35400', '#E74C3C'])
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Tamaño de Mercado de Dispositivos Médicos")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Criterios para Expansión o Mantenimiento de Mercados
st.subheader("Criterios para Expandir o Mantener Mercados")

# Mostrar criterios para cada país
for country, size in zip(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)']):
    if size >= 3000:
        st.write(f"**{country}**: El mercado es grande y se debe **mantener** con estrategias actuales.")
    elif size >= 1200:
        st.write(f"**{country}**: Aunque el mercado es pequeño, se recomienda **explorar** nuevas oportunidades.")
    else:
        st.write(f"**{country}**: El mercado es pequeño, pero con un enfoque adecuado se pueden encontrar **nuevas oportunidades**.")

# Gráfico interactivo
st.subheader("Gráfico de los Criterios para Explorar y Mantener Mercados")
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)'], color=['#2ECC71', '#3498DB', '#9B59B6', '#F1C40F', '#E74C3C'])
ax3.set_xlabel("País")
ax3.set_ylabel("Tamaño del Mercado (USD millones)")
ax3.set_title("Tamaño del Mercado y Estrategias por País")
plt.xticks(rotation=45)
st.pyplot(fig3)

