import json
import os
import streamlit as st

# Función para guardar la configuración en un archivo JSON
def guardar_configuracion(configuracion, nombre_archivo):
    # Abre (o crea) el archivo para escritura ('w')
    with open(nombre_archivo, 'w') as f:
        # Guarda el diccionario de configuración como un archivo JSON
        json.dump(configuracion, f)

# Función para cargar la configuración desde un archivo JSON
def cargar_configuracion(nombre_archivo):
    # Abre el archivo para lectura ('r')
    with open(nombre_archivo, 'r') as f:
        # Carga y devuelve el contenido del archivo JSON como un diccionario
        return json.load(f)

# Función para descargar la configuración como un archivo JSON a través de Streamlit
def descargar_configuracion(configuracion, nombre_archivo):
    # Convierte el diccionario de configuración a una cadena JSON con formato indentado
    json_data = json.dumps(configuracion, indent=4)
    # Crea un botón de descarga en la interfaz de Streamlit
    st.download_button(
        label="Descargar configuración",  # Etiqueta del botón
        data=json_data,                   # Datos del archivo JSON
        file_name=nombre_archivo,         # Nombre del archivo a descargar
        mime="application/json",          # Tipo MIME del archivo
    )
