import streamlit as st

st.set_page_config(page_title="Proteínas", page_icon="🧬", layout="wide")

# ---------------------
# MENÚ PRINCIPAL
# ---------------------
st.title("🧬 Introducción a las Proteínas")

st.markdown("""
Elaborado por: **Yuliana Dórame Félix** y **Jorge Alberto Duran Fuentes**
""")

st.markdown("""
## ¿Qué son las proteínas?
Las proteínas son macromoléculas esenciales formadas por cadenas de aminoácidos. Participan en prácticamente todos los procesos del cuerpo humano: desde la estructura y reparación de tejidos hasta la regulación del metabolismo y la defensa inmunológica.
""")

st.markdown("---")

# Selección del apartado
opcion = st.selectbox(
    "Selecciona el tipo de proteína que deseas visualizar:",
    [
        "📌 Selecciona una opción",
        "🧵 Proteínas Fibrosas",
        "⚪ Proteínas Globulares",
        "🧱 Proteínas de Membrana",
        "💪 Proteínas Motoras",
        "📦 Proteínas de Almacenamiento",
        "⚙️ Proteínas Reguladoras"
    ]
)

st.markdown("---")

# --------------------------
# CONTENIDO SEGÚN OPCIÓN
# --------------------------

# 1. FIBROSAS
if opcion == "🧵 Proteínas Fibrosas":
    st.header("🧵 Proteínas Fibrosas")
    st.markdown("""
Las proteínas fibrosas se caracterizan por presentar estructuras largas, alargadas y con forma de fibras. 
Son altamente resistentes y cumplen funciones principalmente estructurales, proporcionando soporte y elasticidad 
a tejidos como la piel, músculos, tendones y cabello.

### Características:
- Estructura alargada y resistente  
- Función estructural  
- Ejemplos: **Colágeno, Queratina, Fibrina**  
""")
    st.image("https://mibepharma.com/fileadmin/_processed_/5/1/csm_Que-es-el-Colageno_a220342844.jpg", caption="Estructura tridimensional digitalizada del colágeno")
    st.image("https://www.shutterstock.com/image-illustration/example-keratin-structure-fibrous-structural-260nw-510065677.jpg", caption="Estructura tridimensional digitalizada de la queratina")


# 2. GLOBULARES
elif opcion == "⚪ Proteínas Globulares":
    st.header("⚪ Proteínas Globulares")
    st.markdown("""
Las proteínas globulares tienen una estructura compacta y esférica que les permite participar en procesos 
dinámicos dentro del organismo. Suelen ser solubles en agua y desempeñan funciones como transporte, catálisis 
y regulación celular.

### Características:
- Forma esférica  
- Funciones dinámicas  
- Ejemplos: **Hemoglobina, Mioglobina, Enzimas**  
""")
    st.image("https://us.mozaweb.com/es/mozaik3D/KEM/szerves/hemoglobin/preview/Molekula.jpg", caption="Estructura digitalizada de la hemoglobina")
    st.image("https://www.shutterstock.com/image-illustration/pepsin-3d-model-enzyme-that-260nw-108250013.jpg", caption="Estructura digitalizada de la enzima pepsina")


# 3. MEMBRANA
elif opcion == "🧱 Proteínas de Membrana":
    st.header("🧱 Proteínas de Membrana")
    st.markdown("""
Las proteínas de membrana están incrustadas o asociadas a la membrana celular, donde desempeñan funciones 
vitales como transporte, señalización y comunicación.

### Características:
- Asociadas a la membrana celular  
- Transporte de sustancias  
- Ejemplos: **Canales iónicos, GPCR, Bombas ATPasa**  
""")
    st.image("https://media.istockphoto.com/id/1333139388/es/foto/canal-iónico-en-la-membrana-celular.jpg", caption="Representación digitalizada de un canal iónico")


# 4. MOTORAS
elif opcion == "💪 Proteínas Motoras":
    st.header("💪 Proteínas Motoras")
    st.markdown("""
Las proteínas motoras son responsables del movimiento dentro de las células y del desplazamiento de estructuras 
completas como los músculos. Utilizan ATP como fuente de energía.

### Características:
- Permiten movimiento celular  
- Ejemplos: **Actina, Miosina, Dineína, Quinesina**  
""")
    st.image("https://www.lifeder.com/wp-content/uploads/2019/05/miosina.jpg", caption="Representación de la miosina")


# 5. ALMACENAMIENTO
elif opcion == "📦 Proteínas de Almacenamiento":
    st.header("📦 Proteínas de Almacenamiento")
    st.markdown("""
Estas proteínas guardan nutrientes esenciales como aminoácidos o minerales para su uso posterior.

### Características:
- Reservan sustancias  
- Ejemplos: **Ferritina, Caseína**  
""")
    st.image("https://www.researchgate.net/publication/337519666/figure/fig2/AS:11431281109081296@1671736572353/Figura-2-Estructura-de-la-ferritina-en-la-que-se-muestra-la-disposicion-de-las.png",
             caption="Estructura digitalizada de la ferritina")


# 6. REGULADORAS
elif opcion == "⚙️ Proteínas Reguladoras":
    st.header("⚙️ Proteínas Reguladoras")
    st.markdown("""
Las proteínas reguladoras controlan procesos biológicos como la expresión génica o la actividad enzimática.

### Características:
- Controlan funciones celulares  
- Ejemplos: **Factores de transcripción, represores**  
""")
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/72/1FOS.png",
             caption="Factor de transcripción AP-1")
