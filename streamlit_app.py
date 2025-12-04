import streamlit as st
st.set_page_config(page_title="Inicio - Proteínas", page_icon="🧬", layout="wide")

def main():
    st.title(" 🧬 Introducción a las Proteínas")
    st.markdown("""
    Elaborado por: Yuliana Dórame Félix y Jorge Alberto Duran Fuentes
    """)
    st.markdown("""
    ## ¿Qué son las proteínas?
    Las proteínas son macromoléculas esenciales formadas por cadenas de aminoácidos. Participan en prácticamente todos los procesos del cuerpo humano: desde la estructura y reparación de tejidos hasta la regulación del metabolismo y la defensa inmunológica.
    Son uno de los tres macronutrientes principales, junto con los carbohidratos y las grasas. Se clasifican en: 
    - Estructurales
    - Catalíticas (enzimas)
    - De transporte
    - De señalización
    - De defensa

    """)
    
    st.markdown("""
    ---
    ## Ejemplos de tipos de proteínas

    ### 1. Proteínas Fibrosas
    Las proteínas fibrosas se caracterizan por presentar estructuras largas, alargadas y con forma de fibras. Son altamente resistentes y desempeñan funciones principalmente estructurales, proporcionando soporte y elasticidad a tejidos como la piel, músculos, tendones y cabello. Ejemplos importantes incluyen el colágeno, la queratina y la elastina, que conforman gran parte del armazón del cuerpo.
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
    Las proteínas globulares tienen una estructura compacta y esférica que les permite participar en procesos dinámicos dentro del organismo. Suelen ser solubles en agua y desempeñan funciones como transporte, catálisis de reacciones químicas y regulación celular. Ejemplos de este tipo son las enzimas, anticuerpos y hormonas proteicas, todas esenciales para mantener el equilibrio fisiológico.

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
    Las proteínas de membrana están incrustadas o asociadas a la membrana celular, donde cumplen funciones vitales como el transporte de moléculas, la transmisión de señales y el mantenimiento de la estructura celular. Pueden atravesar la membrana o ubicarse en su superficie interna o externa, permitiendo la comunicación entre el interior de la célula y su entorno.

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
    Las proteínas motoras son responsables del movimiento dentro de las células y del desplazamiento de estructuras completas como los músculos. Utilizan energía, normalmente en forma de ATP, para generar cambios conformacionales que producen movimiento. Entre las más importantes se encuentran la miosina, la quinesina y la dineína, esenciales para el transporte intracelular y la contracción muscular.

    - Permiten el movimiento celular
    - Ejemplos: Actina, Miosina, Dineína, Kinesina
    
    """)
    st.image("https://www.lifeder.com/wp-content/uploads/2019/05/miosina.jpg")
    st.markdown(""" Representación digitalizada de miosina.
    """)
    st.markdown("""
    ---
    ### 5. Proteínas de Almacenamiento
    Las proteínas de almacenamiento se encargan de acumular y conservar nutrientes, especialmente aminoácidos y minerales esenciales, para ser utilizados posteriormente por el organismo o por células en crecimiento. Ejemplos comunes son la ferritina, que almacena hierro en animales, y las proteínas de reserva presentes en semillas como la gliadina o la zeína.

    - Guardan iones o moléculas para usarse después
    - Ejemplos: Ferritina, Caseína

    """)
    st.image("https://www.researchgate.net/publication/337519666/figure/fig2/AS:11431281109081296@1671736572353/Figura-2-Estructura-de-la-ferritina-en-la-que-se-muestra-la-disposicion-de-las.png")
    st.markdown(""" Representación digitalizada de ferritina.
    """)
    st.markdown("""
    ---
    ### 6. Proteínas Reguladoras
    Las proteínas reguladoras participan en el control y coordinación de procesos biológicos. Actúan activando o inhibiendo funciones específicas, regulando la expresión génica, modulando rutas metabólicas o controlando el ciclo celular. Entre estas proteínas se encuentran los factores de transcripción, algunas hormonas y proteínas que responden a señales del ambiente.

    - Controlan la expresión génica y otras actividades celulares
    - Ejemplos: Factores de transcripción, represores, proteínas activadoras

    *Aquí irá una imagen de un factor de transcripción*
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/72/1FOS.png")
    st.markdown(""" Representación de factor de transcripción AP-1.
    """)
if __name__ == "__main__":
    main()
