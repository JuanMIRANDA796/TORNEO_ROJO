import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración inicial del Dashboard
st.set_page_config(page_title='Torneo_ROJO', layout='wide')

st.title("Información del torneo ⚽")

st.write("Nea esta página se crea para dar toda la información del torneo que se jugará el próximo Viernes, la idea es que la información de la página se vaya actualizando a medida que los equipos se vayan inscribiendo y a medida en que el torneo esté transcurriendo.")

# Menú lateral para navegación
st.sidebar.title("📌 Menú de Opciones")
option = st.sidebar.radio("Selecciona una opción", ["Equipos", "Tabla de posiciones", "Esquema del Torneo", "Premiación", "Inscripción"])

# Configuración de acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('just-armor-452506-q7-207eaab47fa8.json', scope)
client = gspread.authorize(creds)

# Función para cargar datos de Google Sheets usando la URL
def load_data(sheet_name):
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1ibU57_4hTSA79oE-B8M9Se5f7A0uHi9nr_VJtPmcpRE/edit#gid=506641729'
    sheet = client.open_by_url(spreadsheet_url).worksheet(sheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Mostrar datos en la opción "Equipos"
if option == "Equipos":
    st.subheader("Equipos Inscritos")
    equipos_df = load_data("R_1")
    st.dataframe(equipos_df)
