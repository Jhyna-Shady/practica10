import streamlit as st

# Importa las clases necesarias
from recursos_streamlit.superficies import Plano, Paraboloide, Sinusoide
from recursos_streamlit.visualizador import Visualizador3DPlotly

def main():
    st.title("Visualización en 3D")
    st.subheader("Elija el cuerpo geométrico")

    # Menú de selección
    tipo = st.radio("Seleccione una opción", ["Plano", "Paraboloide", "Sinusoide"])

    # Configuración de parámetros basada en la selección
    if tipo == "Plano":
        pendiente = st.slider("Ingrese la pendiente del plano:", min_value=-10.0, max_value=10.0, value=1.0)
        superficie = Plano((-5, 5), (-5, 5), pendiente)
    elif tipo == "Paraboloide":
        coef = st.slider("Ingrese el coeficiente del paraboloide:", min_value=0.1, max_value=10.0, value=1.0)
        superficie = Paraboloide((-5, 5), (-5, 5), coef)
    elif tipo == "Sinusoide":
        frecuencia = st.slider("Ingrese la frecuencia de la sinusoide:", min_value=0.1, max_value=10.0, value=1.0)
        superficie = Sinusoide((-5, 5), (-5, 5), frecuencia)
    else:
        st.error("Opción no válida.")
        return

    # Visualización
    visualizador = Visualizador3DPlotly(superficie)
    visualizador.mostrar_con_plotly()

if __name__ == "__main__":
    main()
