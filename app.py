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

# Mostrar la tabla de segmentos de clientes
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

# Mostrar la tabla de exportaciones
st.subheader("Exportaciones (USD millones)")
st.dataframe(df_exportaciones)

# Gráfico de exportaciones
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(df_exportaciones['País'], df_exportaciones['Exportaciones (USD millones)'], color=['#2ECC71', '#3498DB', '#9B59B6', '#F1C40F', '#E74C3C'])
ax3.set_xlabel("País")
ax3.set_ylabel("Exportaciones (USD millones)")
ax3.set_title("Exportaciones de Dispositivos Médicos por País")
plt.xticks(rotation=45)
st.pyplot(fig3)

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

# Gráfico interactivo de los criterios para explorar y mantener mercados
st.subheader("Gráfico de los Criterios para Explorar y Mantener Mercados")
fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.bar(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)'], color=['#2ECC71', '#3498DB', '#9B59B6', '#F1C40F', '#E74C3C'])
ax4.set_xlabel("País")
ax4.set_ylabel("Tamaño del Mercado (USD millones)")
ax4.set_title("Tamaño del Mercado y Estrategias por País")
plt.xticks(rotation=45)
st.pyplot(fig4)


