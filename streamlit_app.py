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

    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Myoglobin.png/500px-Myoglobin.png")
    st.markdown(""" Representación de la estructura tridimensional digitalizada de la mioglobina
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
    st.image("https://p.turbosquid.com/ts-thumb/C6/e4tgBo/wtWWOLy1/collagenturn20000/jpg/1500673045/1920x1080/fit_q87/fbec05175396c9e2052cfa48fc31aa5bd90e061f/collagenturn20000.jpg")
    st.markdown(""" Representación de la estructura tridimensional digitalizada del colágeno
    """)
    st.image("https://www.shutterstock.com/image-illustration/example-keratin-structure-fibrous-structural-260nw-510065677.jpg")
    st.markdown(""" Representación de la estructura tridimensional digitalizada de la queratina
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
