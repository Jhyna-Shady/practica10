import streamlit as st
import json
from recursos_streamlit.superficies import Plano, Paraboloide, Sinusoide, Hiperboloide, Esfera
from recursos_streamlit.visualizador import Visualizador3DPlotly
from recursos_streamlit.configuraciones import guardar_configuracion, descargar_configuracion, cargar_configuracion

def main():
    # Título de la aplicación
    st.title("Visualización en 3D")
    st.subheader("Elija el cuerpo geométrico")

    # Menú de selección para elegir el tipo de superficie
    tipo = st.radio("Seleccione una opción", ["Plano", "Paraboloide", "Sinusoide", "Hiperboloide", "Esfera"])

    # Configuración de parámetros basada en la selección
    if tipo == "Plano":
        pendiente = st.slider("Ingrese la pendiente del plano:", min_value=-10.0, max_value=10.0, value=1.0)
        superficie = Plano((-15, 15), (-15, 15), pendiente)
    elif tipo == "Paraboloide":
        coef = st.slider("Ingrese el coeficiente del paraboloide:", min_value=0.1, max_value=10.0, value=1.0)
        superficie = Paraboloide((-15, 15), (-15, 15), coef)
    elif tipo == "Sinusoide":
        frecuencia = st.slider("Ingrese la frecuencia de la sinusoide:", min_value=0.1, max_value=10.0, value=1.0)
        superficie = Sinusoide((-15, 15), (-15, 15), frecuencia)
    elif tipo == "Hiperboloide":
        a = st.slider("Ingrese el valor de 'a' del hiperboloide:", min_value=0.1, max_value=10.0, value=1.0)
        b = st.slider("Ingrese el valor de 'b' del hiperboloide:", min_value=0.1, max_value=10.0, value=1.0)
        c = st.slider("Ingrese el valor de 'c' del hiperboloide:", min_value=0.1, max_value=10.0, value=1.0)
        superficie = Hiperboloide((-15, 15), (-15, 15), a, b, c)
    elif tipo == "Esfera":
        radio = st.slider("Ingrese el radio de la esfera:", min_value=0.1, max_value=10.0, value=1.0)
        superficie = Esfera((-15, 15), (-15, 15), radio)
    else:
        st.error("Opción no válida.")
        return

    # Guardar configuración
    if st.button("Guardar configuración"):
        configuracion = {
            'tipo': tipo,
            'parametros': {
                'pendiente': pendiente if tipo == "Plano" else None,
                'coef': coef if tipo == "Paraboloide" else None,
                'frecuencia': frecuencia if tipo == "Sinusoide" else None,
                'a': a if tipo == "Hiperboloide" else None,
                'b': b if tipo == "Hiperboloide" else None,
                'c': c if tipo == "Hiperboloide" else None,
                'radio': radio if tipo == "Esfera" else None,
            }
        }
        # Generar nombre de archivo basado en el tipo de superficie
        nombre_archivo = f"{tipo.lower().replace(' ', '_')}_configuracion.json"
        guardar_configuracion(configuracion, nombre_archivo)
        st.success(f"Configuración guardada en {nombre_archivo}")
        descargar_configuracion(configuracion, nombre_archivo)  # Llama a la función para descargar el archivo JSON

    # Cargar configuración
    uploaded_file = st.file_uploader("Cargar configuración desde archivo JSON:")
    if uploaded_file is not None:
        contenido = uploaded_file.getvalue()
        configuracion = json.loads(contenido)
        st.write(configuracion)
        if configuracion['tipo'] == "Plano":
            superficie = Plano((-15, 15), (-15, 15), configuracion['parametros']['pendiente'])
        elif configuracion['tipo'] == "Paraboloide":
            superficie = Paraboloide((-15, 15), (-15, 15), configuracion['parametros']['coef'])
        elif configuracion['tipo'] == "Sinusoide":
            superficie = Sinusoide((-15, 15), (-15, 15), configuracion['parametros']['frecuencia'])
        elif configuracion['tipo'] == "Hiperboloide":
            superficie = Hiperboloide((-15, 15), (-15, 15), configuracion['parametros']['a'], configuracion['parametros']['b'], configuracion['parametros']['c'])
        elif configuracion['tipo'] == "Esfera":
            superficie = Esfera((-15, 15), (-15, 15), configuracion['parametros']['radio'])

    # Visualización
    visualizador = Visualizador3DPlotly(superficie)
    visualizador.mostrar_con_plotly()

if __name__ == "__main__":
    main()
