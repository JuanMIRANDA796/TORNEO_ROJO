import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import io

# Configuración inicial del Dashboard
st.set_page_config(page_title='Torneo_ROJO', layout='wide')

st.title("Información del torneo ⚽")

st.write("Nea esta pagina se crea para dar toda la informción del torneo que se jugara el proximo Viernes, la idea es que la información de la pagina se vaya actualizando a medida que los equipos de vayan inscribiendo y a medida en que el torneo este transcurriendo")

# Menú lateral para navegación
st.sidebar.title("📌 Menú de Opciones")
option = st.sidebar.radio("Selecciona una opción", ["Equipos ", "Tabla de posiciones", "Esquema del Torneo", "Premiación", "Inscripción"])
