import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
from pathlib import Path

#1. Configuración inicial de la aplicación

st.set_page_config(
  page_title = "TORNEO ECONOMICAS ⚽",
  page_icon = " "
)
st.title("TORNEO ECONOMICAS 🍀⚽🍀")
st.sidebar.title("Opciones de navegación")

menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Equipos", "Inscripción", "Premiación", "Información general"]
)

# Ruta de la imagen y el archivo de música
image_path = Path.home() / "Downloads" / "image(4).png"  # Cambia 'nombre_de_tu_imagen.png' por el nombre de tu imagen
#audio_path = Path.home() / "Downloads" / "nombre_de_tu_audio.mp3"   # Cambia 'nombre_de_tu_audio.mp3' por el nombre de tu archivo de audio

#2. Mostrar la imagen y reproducir el audio en la opción de inicio
if menu == "Inicio":
    st.header("Bienvenido al Torneo Económicas")
    
    # Leer y mostrar la imagen desde la carpeta de descargas
    with open(image_path, "rb") as image_file:
        st.image(image_file, caption="Imagen cargada")
    
    # Leer y reproducir el archivo de audio desde la carpeta de descargas
    #with open(audio_path, "rb") as audio_file:
     #   st.audio(audio_file)
