import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

#1. Configuración inical de la aplicacion

st.set_page_config(
  page_title = "TORNEO ECONOMICAS ⚽",
  page_icon = " "
)
st.title("TORNEO ECONOMICAS 🍀⚽🍀")
st.sidebar.title("Opciones de  navegación")

menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Equipos", "Inscripción", "Premiación", "Información general"]
)

