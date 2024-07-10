import json
import os
import streamlit as st

def guardar_configuracion(configuracion, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        json.dump(configuracion, f)

def cargar_configuracion(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return json.load(f)

def descargar_configuracion(configuracion, nombre_archivo):
    json_data = json.dumps(configuracion, indent=4)
    st.download_button(
        label="Descargar configuración",
        data=json_data,
        file_name=nombre_archivo,
        mime="application/json",
    )
    
