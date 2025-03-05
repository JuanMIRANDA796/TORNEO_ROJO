import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración inicial del Dashboard
st.set_page_config(page_title='Torneo_ROJO', layout='wide')

# Agregar estilo CSS con la fuente Rock Salt
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rock+Salt&display=swap');

    .title {
        font-family: 'Rock Salt', cursive;
        font-size: 40px;
        color: #f63366;
        text-align: center;
        font-weight: bold;
    }
    .text {
        font-family: 'Rock Salt', cursive;
        font-size: 16px;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Título del Dashboard
st.markdown('<p class="title">Información del torneo ⚽</p>', unsafe_allow_html=True)

st.markdown('<p class="text">Nea esta página se crea para dar toda la información del torneo que se jugará el próximo Viernes, la idea es que la información de la página se vaya actualizando a medida que los equipos se vayan inscribiendo y a medida en que el torneo esté transcurriendo.</p>', unsafe_allow_html=True)

# Menú lateral para navegación
st.sidebar.title("📌 Menú de Opciones")
option = st.sidebar.radio("Selecciona una opción", ["Equipos", "Tabla de posiciones", "Esquema del Torneo", "Premiación", "Inscripción"])

# Mostrar la tabla de equipos cuando se selecciona la opción "Equipos"
if option == "Equipos":
    st.header("Equipos Participantes")
    # Leer el archivo CSV desde la URL
    url = 'https://raw.githubusercontent.com/JuanMIRANDA796/TORNEO_ROJO/refs/heads/main/INSCRIPCIÓN%20(respuestas)%20-%20R_1.csv'
    df = pd.read_csv(url)
    # Mostrar la tabla en el Dashboard
    st.dataframe(df)
