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
        page_icon = "⚽"
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
        st.header("Nea pille pues, en esta pagina va a estar toda la información con respecto al torneo que se jugara este Viernes")
        
        # Leer y mostrar la imagen desde la carpeta de descargas
        #try:
         #   with open(image_path, "rb") as image_file:
          #      st.image(image_file, caption="Imagen cargada")
        #except FileNotFoundError:
         #   st.error("El archivo de imagen no se encontró en la ruta especificada.")
        
        # Leer y reproducir el archivo de audio desde la carpeta de descargas
        #try:
         #   with open(audio_path, "rb") as audio_file:
          #      st.audio(audio_file)
        #except FileNotFoundError:
         #   st.error("El archivo de audio no se encontró en la ruta especificada.")
    
    elif menu == "Equipos":
        st.header("Equipos Inscritos, a medida en que se vayan inscribiendo los equipos la base de datos se va actualizando")
        
        # Consulta para obtener los equipos de la base de datos
        tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
        st.sidebar.write("### 📌 Tablas disponibles en la base de datos:")
        st.sidebar.write(tables)

        # Selección de tabla para visualizar
        table_name = st.sidebar.selectbox("Selecciona una tabla para ver los datos:", tables["name"])

        if table_name:
            # Cargar los datos en un DataFrame
            df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            st.write(f"### 📊 Datos de la tabla `{table_name}`")
            st.dataframe(df)

    elif menu == "Inscripción":
        st.header("Inscripción")
        st.markdown("""
        1. En el siguiente link se podrá hacer la inscripción de los equipos, por equipo máximo se admitirán 8 personas.
        2. El valor de la inscripción es 70K por equipo.
        """)
        st.markdown("[Formulario de Inscripción](https://docs.google.com/forms/d/e/1FAIpQLSdhDNtJESBn-JohTgYkrALun3MfsulqyTos-uOF-wvV-AWRDg/viewform?usp=header)", unsafe_allow_html=True)

    elif menu == "Premiación":
        st.header("Premiación")
        st.markdown("""
        Luego de saber la cantidad de equipos se recogerá todo el dinero y se dividirá de la siguiente manera:
        1. El Campeón se lleva el 70% del dinero recogido.
        2. El subcampeón se llevará el 30% del dinero recogido.
        """)

    elif menu == "Información general":
        st.header("Información general")
        st.markdown("""
        1. El torneo se jugará en las canchas del metro de la U.
        2. El dinero se recogerá el mismo día del torneo.
        3. La hora de inicio está por confirmar.
        """)

    # Cerrar la conexión a la base de datos
    conn.close()
