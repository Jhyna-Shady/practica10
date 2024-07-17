import streamlit as st  # Importa la librería Streamlit para crear interfaces web interactivas.
import json  # Importa la librería json para trabajar con archivos JSON.
from recursos_streamlit.superficies import Plano, Paraboloide, Sinusoide, Hiperboloide, Esfera  # Importa las clases de diferentes superficies geométricas.
from recursos_streamlit.visualizador import Visualizador3DPlotly  # Importa la clase para visualizar superficies en 3D usando Plotly.
from recursos_streamlit.configuraciones import guardar_configuracion, descargar_configuracion, cargar_configuracion  # Importa funciones para manejar configuraciones.

def main():
    # Título de la aplicación
    st.title("Visualización en 3D")  # Establece el título de la aplicación en la interfaz de usuario.
    st.subheader("Elija el cuerpo geométrico")  # Añade un subtítulo que indica al usuario que elija un cuerpo geométrico.

    # Menú de selección para elegir el tipo de superficie
    tipo = st.radio("Seleccione una opción", ["Plano", "Paraboloide", "Sinusoide", "Hiperboloide", "Esfera"])  # Crea un menú de radio buttons para seleccionar el tipo de superficie.

    # Configuración de parámetros basada en la selección
    if tipo == "Plano":  # Si se selecciona "Plano":
        pendiente = st.slider("Ingrese la pendiente del plano:", min_value=-10.0, max_value=10.0, value=1.0)  # Deslizador para elegir la pendiente del plano.
        superficie = Plano((-15, 15), (-15, 15), pendiente)  # Crea una instancia de la clase Plano con los parámetros seleccionados.
    elif tipo == "Paraboloide":  # Si se selecciona "Paraboloide":
        coef = st.slider("Ingrese el coeficiente del paraboloide:", min_value=0.1, max_value=10.0, value=1.0)  # Deslizador para elegir el coeficiente del paraboloide.
        superficie = Paraboloide((-15, 15), (-15, 15), coef)  # Crea una instancia de la clase Paraboloide con los parámetros seleccionados.
    elif tipo == "Sinusoide":  # Si se selecciona "Sinusoide":
        frecuencia = st.slider("Ingrese la frecuencia de la sinusoide:", min_value=0.1, max_value=10.0, value=1.0)  # Deslizador para elegir la frecuencia de la sinusoide.
        superficie = Sinusoide((-15, 15), (-15, 15), frecuencia)  # Crea una instancia de la clase Sinusoide con los parámetros seleccionados.
    elif tipo == "Hiperboloide":  # Si se selecciona "Hiperboloide":
        a = st.slider("Ingrese el valor de 'a' del hiperboloide:", min_value=0.1, max_value=10.0, value=1.0)  # Deslizador para elegir el valor de 'a'.
        b = st.slider("Ingrese el valor de 'b' del hiperboloide:", min_value=0.1, max_value=10.0, value=1.0)  # Deslizador para elegir el valor de 'b'.
        c = st.slider("Ingrese el valor de 'c' del hiperboloide:", min_value=0.1, max_value=10.0, value=1.0)  # Deslizador para elegir el valor de 'c'.
        superficie = Hiperboloide((-15, 15), (-15, 15), a, b, c)  # Crea una instancia de la clase Hiperboloide con los parámetros seleccionados.
    elif tipo == "Esfera":  # Si se selecciona "Esfera":
        radio = st.slider("Ingrese el radio de la esfera:", min_value=0.1, max_value=10.0, value=1.0)  # Deslizador para elegir el radio de la esfera.
        superficie = Esfera((-15, 15), (-15, 15), radio)  # Crea una instancia de la clase Esfera con los parámetros seleccionados.
    else:
        st.error("Opción no válida.")  # Muestra un mensaje de error si la opción seleccionada no es válida.
        return  # Termina la ejecución de la función.

    # Guardar configuración
    if st.button("Guardar configuración"):  # Si se presiona el botón "Guardar configuración":
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
        }  # Crea un diccionario con la configuración actual basada en el tipo de superficie y sus parámetros.
        nombre_archivo = f"{tipo.lower().replace(' ', '_')}_configuracion.json"  # Genera un nombre de archivo basado en el tipo de superficie.
        guardar_configuracion(configuracion, nombre_archivo)  # Llama a la función para guardar la configuración en un archivo JSON.
        st.success(f"Configuración guardada en {nombre_archivo}")  # Muestra un mensaje de éxito con el nombre del archivo guardado.
        descargar_configuracion(configuracion, nombre_archivo)  # Llama a la función para descargar el archivo JSON.

    # Cargar configuración
    uploaded_file = st.file_uploader("Cargar configuración desde archivo JSON:")  # Permite al usuario subir un archivo JSON con la configuración.
    if uploaded_file is not None:  # Si se ha subido un archivo:
        contenido = uploaded_file.getvalue()  # Lee el contenido del archivo.
        configuracion = json.loads(contenido)  # Carga el contenido JSON en un diccionario.
        st.write(configuracion)  # Muestra el contenido del archivo JSON.
        if configuracion['tipo'] == "Plano":  # Si el tipo es "Plano":
            superficie = Plano((-15, 15), (-15, 15), configuracion['parametros']['pendiente'])  # Crea una instancia de Plano con la configuración cargada.
        elif configuracion['tipo'] == "Paraboloide":  # Si el tipo es "Paraboloide":
            superficie = Paraboloide((-15, 15), (-15, 15), configuracion['parametros']['coef'])  # Crea una instancia de Paraboloide con la configuración cargada.
        elif configuracion['tipo'] == "Sinusoide":  # Si el tipo es "Sinusoide":
            superficie = Sinusoide((-15, 15), (-15, 15), configuracion['parametros']['frecuencia'])  # Crea una instancia de Sinusoide con la configuración cargada.
        elif configuracion['tipo'] == "Hiperboloide":  # Si el tipo es "Hiperboloide":
            superficie = Hiperboloide((-15, 15), (-15, 15), configuracion['parametros']['a'], configuracion['parametros']['b'], configuracion['parametros']['c'])  # Crea una instancia de Hiperboloide con la configuración cargada.
        elif configuracion['tipo'] == "Esfera":  # Si el tipo es "Esfera":
            superficie = Esfera((-15, 15), (-15, 15), configuracion['parametros']['radio'])  # Crea una instancia de Esfera con la configuración cargada.

    # Visualización
    visualizador = Visualizador3DPlotly(superficie)  # Crea una instancia del visualizador 3D con la superficie seleccionada.
    visualizador.mostrar_con_plotly()  # Llama al método para mostrar la superficie en 3D usando Plotly.

if __name__ == "__main__":
    main()  # Llama a la función principal cuando se ejecuta el script.
