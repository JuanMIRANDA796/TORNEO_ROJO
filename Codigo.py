import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
from pathlib import Path
import sqlite3
import requests

# URL del archivo de base de datos SQLite en GitHub
GITHUB_DB_URL = "https://raw.githubusercontent.com/JuanMIRANDA796/TORNEO_ROJO/main/inscripcion.db"

# Función para descargar y guardar el archivo de base de datos
def descargar_db(url, filename="inscripcion.db"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        return filename
    else:
        st.error("⚠️ Error al descargar el archivo de base de datos desde GitHub.")
        return None

# Descargar el archivo de base de datos
db_file = descargar_db(GITHUB_DB_URL)

# Conectar a la base de datos SQLite
if db_file:
    conn = sqlite3.connect(db_file)

    # Configuración inicial de la aplicación
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
    image_path = r"C:\Users\Juan\Downloads\image (4).png"  # Ruta específica de la imagen con cadena sin procesar
    #audio_path = r"C:\Users\Juan\Downloads\nombre_de_tu_audio.mp3"  # Cambia 'nombre_de_tu_audio.mp3' por el nombre de tu archivo de audio

    # Mostrar contenido según la opción seleccionada
    if menu == "Inicio":
        st.header("Nea pille pues, en esta pagina va a estar toda la información con respecto  a el torneo que se jugara este Viernes")
        
        # Leer y mostrar la imagen desde la carpeta de descargas
        try:
            with open(image_path, "rb") as image_file:
                st.image(image_file, caption="Imagen cargada")
        except FileNotFoundError:
            st.error("El archivo de imagen no se encontró en la ruta especificada.")
        
        # Leer y reproducir el archivo de audio desde la carpeta de descargas
        #try:
         #   with open(audio_path, "rb") as audio_file:
          #      st.audio(audio_file)
        #except FileNotFoundError:
         #   st.error("El archivo de audio no se encontró en la ruta especificada.")
    
    elif menu == "Equipos":
        st.header("Equipos Inscritos, a medida en que se vayan inscribiendo los equipos la base de datos se va actualizando")
        
        # Consulta para obtener los equipos de la base de datos
        query = "SELECT * FROM inscripcion"  # Asegúrate de que la tabla se llame 'equipos'
        
        try:
            df_equipos = pd.read_sql(query, conn)
            st.write(df_equipos)
        except Exception as e:
            st.error(f"Error al obtener los equipos: {e}")
        
        # También puedes mostrar algunos gráficos si tienes datos suficientes
    
