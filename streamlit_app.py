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
    st.markdown(""" Representación de la estructura tridimensional digitalizada de la mioglobina.
    """)
    st.markdown("""
    ---
    ## Ejemplos de tipos de proteínas

    ### 1. Proteínas Fibrosas
    - Estructura alargada y resistente
    - Función estructural
    - Ejemplos: Colágeno, Queratina, Fibrina
    """)
    st.image("https://mibepharma.com/fileadmin/_processed_/5/1/csm_Que-es-el-Colageno_a220342844.jpg")
    st.markdown(""" Representación de la estructura tridimensional digitalizada del colágeno.
    """)
    st.image("https://www.shutterstock.com/image-illustration/example-keratin-structure-fibrous-structural-260nw-510065677.jpg")
    st.markdown(""" Representación de la estructura tridimensional digitalizada de la queratina.
    """)
    st.markdown("""
    ---
    ### 2. Proteínas Globulares
    - Forma esférica
    - Funciones dinámicas y catalíticas
    - Ejemplos: Hemoglobina, Mioglobina, Enzimas

    """)
    st.image("https://us.mozaweb.com/es/mozaik3D/KEM/szerves/hemoglobin/preview/Molekula.jpg")
    st.markdown(""" Representación de la estructura tridimensional digitalizada de la hemoglobina.
    """)
    st.image("https://www.shutterstock.com/image-illustration/pepsin-3d-model-enzyme-that-260nw-108250013.jpg")
    st.markdown(""" Representación de la estructura tridimensional digitalizada de la enzima pepsina.
    """)
    st.markdown("""
    ---
    ### 3. Proteínas de Membrana
    - Se encuentran incrustadas en la membrana celular
    - Permiten transporte, señalización y comunicación celular
    - Ejemplos: Canales iónicos, GPCR, Bombas ATPasa

    """)
    st.image("https://media.istockphoto.com/id/1333139388/es/foto/canal-iónico-en-la-membrana-celular.jpg?s=612x612&w=0&k=20&c=M7maeDkFLnE_o7Sv8rJqcqypuxU3luavc_HOm9egO0k=")
    st.markdown(""" Representación digitalizada de un canal iónico.
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
