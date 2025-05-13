import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo para exportaciones
data_exportaciones = {
    'País': ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Panamá'],
    'Exportaciones (USD millones)': [4291.2, 1416.4, 10450.0, 3440.0, 8768.0]
}

df_exportaciones = pd.DataFrame(data_exportaciones)

# Datos de ejemplo para segmentar mercados
data_segmentos = {
    'País': ['Estados Unidos', 'México', 'Colombia', 'Brasil', 'Argentina'],
    'Tamaño del Mercado (USD millones)': [5000, 1500, 1200, 3000, 700],
    'Criterio': ['Mantener Mercado Actual', 'Explorar Nuevos Mercados', 'Explorar Nuevos Mercados', 'Mantener Mercado Actual', 'Explorar Nuevos Mercados']
}

df_segmentos = pd.DataFrame(data_segmentos)

# Título con emoji
st.title("📊 Dashboard de Exportaciones en Centroamérica")

# Mostrar la tabla de exportaciones
st.subheader("Exportaciones de Dispositivos Médicos")
st.dataframe(df_exportaciones)

# Gráfico de barras con las exportaciones
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_exportaciones['País'], df_exportaciones['Exportaciones (USD millones)'], color=['#2E86C1', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8'])
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title("Exportaciones de Dispositivos Médicos en Centroamérica")
plt.xticks(rotation=45)
st.pyplot(fig)

# Criterios para expandir o mantener mercados
st.markdown("### 🌎 Criterios para Expandir o Mantener Mercados")

# Mostrar criterios con una tabla más atractiva
st.subheader("Criterios por País")
st.table(df_segmentos)

# Agregar una leyenda visual interactiva
st.markdown("""
    **Explicación de los criterios:**
    - **Mantener Mercado Actual**: El mercado tiene un tamaño considerable y se recomienda continuar con la estrategia actual.
    - **Explorar Nuevos Mercados**: El tamaño del mercado es pequeño y se recomienda investigar la posibilidad de expansión.
""")

# Gráfico de barras con los tamaños de mercado
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_segmentos['País'], df_segmentos['Tamaño del Mercado (USD millones)'], color=['#58D68D', '#F7DC6F', '#F39C12', '#D35400', '#E74C3C'])
ax.set_xlabel("País")
ax.set_ylabel("Tamaño del Mercado (USD millones)")
ax.set_title("Tamaño del Mercado de Dispositivos Médicos por País")
plt.xticks(rotation=45)
st.pyplot(fig)

# Leyenda mejorada y con formato
st.markdown("""
    ### 🌍 ¿Qué mercado explorar?
    - **Estados Unidos**: El mercado es grande y se debe **mantener** con estrategias actuales.
    - **México**: Aunque el mercado es pequeño, se recomienda **explorar** nuevas oportunidades.
    - **Colombia**: Mercado intermedio, **explorar** nuevas posibilidades de mercado.
    - **Brasil**: Mercado consolidado, debe **mantenerse** con la estrategia actual.
    - **Argentina**: Mercado pequeño, se recomienda **explorar** otros segmentos o mercados.
""")

# Agregar una visualización interactiva y mejorar la presentación
st.markdown("""
    ### 🌍 Resultados de la Evaluación de Mercados:
    - **Estados Unidos**: El mercado tiene un tamaño considerable, mantener y expandir con estrategias de diversificación.
    - **México**: Mercado más pequeño, se recomienda explorar otros segmentos o mercados.
    - **Colombia**: Mercado intermedio, explorar nuevas posibilidades de mercado.
    - **Brasil**: Mercado consolidado, continuar con la estrategia actual.
    - **Argentina**: Potencial de crecimiento, explorar segmentos alternativos.
""")

# Visualización más atractiva
st.markdown("#### 📊 Gráfico de los criterios para explorar y mantener mercados")


