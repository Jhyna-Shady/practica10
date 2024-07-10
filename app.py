import streamlit as st
import pandas as pd

st.title("Visualización en 3D")
st.subheader("Elija el cuerpo geométrico")

# Usar radio buttons en lugar de tabs o selectbox
opcion = st.radio("Seleccione una opción", ["Plano", "Paraboloide", "Sinusoide"])

if opcion == "Plano":
    st.text("Gráfico plano")
    
elif opcion == "Paraboloide":
    st.text("Gráfico de un Paraboloide")

elif opcion == "Sinusoide":
    st.text("Gráfico de un Sinusoide")