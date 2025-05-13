import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo para segmentar mercados
data_segmentos = {
    'País': ['Estados Unidos', 'México', 'Colombia', 'Brasil', 'Argentina'],
    'Tamaño del Mercado (USD millones)': [5000, 1500, 1200, 3000, 700],
    'Criterio': ['Mantener Mercado Actual', 'Explorar Nuevos Mercados', 'Explorar Nuevos Mercados', 'Mantener Mercado Actual', 'Explorar Nuevos Mercados']
}

df_segmentos = pd.DataFrame(data_segmentos)

# Título con imagen de fondo
st.title("🌍 Criterios para Expandir o Mantener Mercados")

# Mostrar criterios con una tabla más atractiva
st.subheader("Criterios por País")
st.table(df_segmentos)

# Agregar una leyenda visual interactiva
st.markdown("""
    **Explicación de los criterios:**
    - **Mantener Mercado Actual**: El mercado tiene un tamaño considerable y se recomienda continuar con la estrategia actual.
    - **Explorar Nuevos Mercados**: El tamaño del mercado es pequeño y se recomienda investigar la posibilidad de expansión.
""")

# Agregar una visualización interactiva
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
    ### 🌎 ¿Qué mercado explorar?
    - **Estados Unidos**: El mercado es grande y se debe **mantener** con estrategias actuales.
    - **México**: Aunque el mercado es pequeño, se recomienda **explorar** nuevas oportunidades.
    - **Colombia**: A pesar del tamaño, es un mercado que puede ser clave en el futuro, se debe **explorar**.
    - **Brasil**: El mercado sigue siendo fuerte, por lo que debe **mantenerse** con las estrategias actuales.
    - **Argentina**: El mercado es pequeño, pero con un enfoque adecuado se pueden encontrar **nuevas oportunidades**.
""")

# Establecer fondo visual o gráficos de contexto si es necesario

