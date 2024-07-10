import plotly.graph_objects as go

class Visualizador3D:
    def __init__(self, superficie):
        self.superficie = superficie

    def mostrar_con_plotly(self):
        x, y, z = self.superficie.generar_datos()
        fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        fig.update_layout(title='Superficie 3D', autosize=False, width=800, height=800)
        return fig

class Visualizador3DPlotly(Visualizador3D):
    def mostrar_con_plotly(self):
        fig = super().mostrar_con_plotly()
        import streamlit as st
        st.plotly_chart(fig)
