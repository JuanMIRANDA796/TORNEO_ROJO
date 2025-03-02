import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import io

# Lee el archivo Excel y lo guarda como CSV
excel_file_path = "C:\\Users\\Juan\\OneDrive\\Documentos\\Doc Juan U\\TORNEO_ROJO\\Equipos.xlsx"
df = pd.read_excel(excel_file_path)
csv_file_path = "C:\\Users\\Juan\\OneDrive\\Documentos\\Doc Juan U\\TORNEO_ROJO\\Equipos.csv"
df.to_csv(csv_file_path, index=False)

# Configuración inicial del Dashboard
st.set_page_config(page_title='Torneo_ROJO', layout='wide')

st.title("Información del torneo ⚽")

st.write("Nea esta pagina se crea para dar toda la informción del torneo que se jugara el proximo Viernes, la idea es que la información de la pagina se vaya actualizando a medida que los equipos de vayan inscribiendo y a medida en que el torneo este transcurriendo")

# Menú lateral para navegación
st.sidebar.title("📌 Menú de Opciones")
option = st.sidebar.radio("Selecciona una opción", ["Equipos ", "Tabla de posiciones", "Esquema del Torneo", "Premiación", "Inscripción"])

# Opción para mostrar los equipos
if option == "Equipos ":
    st.subheader("Equipos inscritos 🏆")
    
    # Cargar el archivo CSV
    uploaded_file = st.file_uploader("Sube el archivo CSV con los equipos", type=["csv"])
    
    if uploaded_file is not None:
        # Leer el archivo CSV
        df = pd.read_csv(uploaded_file)
        
        # Mostrar la tabla de equipos
        st.dataframe(df)

  
