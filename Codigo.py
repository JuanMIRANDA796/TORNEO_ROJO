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

# Configuración de las credenciales y acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('just-armor-452506-q7-3aaa2195ebd9.json', scope)
client = gspread.authorize(creds)

# ID del documento de Google Sheets
sheet_id = '1ibU57_4hTSA79oE-B8M9Se5f7A0uHi9nr_VJtPmcpRE'
sheet_name = 'INSCRIPCIÓN'

def load_google_sheet(sheet_id, sheet_name):
    sheet = client.open_by_key(sheet_id).worksheet(sheet_name)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

if option == "Equipos":
    df = load_google_sheet(sheet_id, sheet_name)
    st.write(df)

# Añade las demás opciones aquí...
