import streamlit as st

st.set_page_config(page_title="Inicio - Proteínas", page_icon="🧬", layout="wide")

def main():
    st.title(" 🧬 Introducción a las Proteínas")

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

    st.markdown("""
    ---
    ## Ejemplos de tipos de proteínas

    ### 1. Proteínas Fibrosas
    - Estructura alargada y resistente
    - Función estructural
    - Ejemplos: Colágeno, Queratina, Fibrina

    *Aquí irá una imagen del colágeno*
    *Aquí irá una imagen de la queratina*
    """)

    st.markdown("""
    ---
    ### 2. Proteínas Globulares
    - Forma esférica
    - Funciones dinámicas y catalíticas
    - Ejemplos: Hemoglobina, Mioglobina, Enzimas

    *Aquí irá una imagen de la hemoglobina*
    *Aquí irá una imagen de una enzima*
    """)

    st.markdown("""
    ---
    ### 3. Proteínas de Membrana
    - Se encuentran incrustadas en la membrana celular
    - Permiten transporte, señalización y comunicación celular
    - Ejemplos: Canales iónicos, GPCR, Bombas ATPasa

    *Aquí irá una imagen de un canal iónico*
    """)

    st.markdown("""
    ---
    ### 4. Proteínas Motoras
    - Permiten el movimiento celular
    - Ejemplos: Actina, Miosina, Dineína, Kinesina

    *Aquí irá una imagen de miosina*
    """)

    st.markdown("""
    ---
    ### 5. Proteínas de Almacenamiento
    - Guardan iones o moléculas para usarse después
    - Ejemplos: Ferritina, Caseína

    *Aquí irá una imagen de ferritina*
    """)

    st.markdown("""
    ---
    ### 6. Proteínas Reguladoras
    - Controlan la expresión génica y otras actividades celulares
    - Ejemplos: Factores de transcripción, represores, proteínas activadoras

    *Aquí irá una imagen de un factor de transcripción*
    """)

if __name__ == "__main__":
    main()
