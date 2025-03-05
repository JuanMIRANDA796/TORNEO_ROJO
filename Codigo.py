import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración inicial del Dashboard
st.set_page_config(page_title='Torneo_ROJO', layout='wide')

# Agregar estilo CSS
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #f63366;
        text-align: center;
        font-weight: bold;
    }
    .header {
        font-size: 24px;
        color: #f63366;
    }
    .text {
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
