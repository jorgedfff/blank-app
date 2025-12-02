import streamlit as st


st.set_page_config(page_title="Inicio - Proteínas", page_icon="🏠", layout="wide")

def main():
    st.title("🏠 Introducción a las Proteínas")

    st.markdown("""
    ## ¿Qué son las proteínas?
    Las proteínas son macromoléculas formadas por cadenas de aminoácidos y desempeñan funciones esenciales en los seres vivos, tales como:
    - Estructurales
    - Catalíticas (enzimas)
    - De transporte
    - De señalización
    - De defensa

    *Aquí irá una imagen representativa general de una proteína (estructura 3D)*
    """)
