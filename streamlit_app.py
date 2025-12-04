import streamlit as st

# --- CONFIGURURACIÓN GENERAL ---
st.set_page_config(page_title="Tipos de Proteínas", layout="wide", page_icon="🧬")

st.title("🧬 Portal Educativo: Tipos de Proteínas")
st.markdown("Explora las principales categorías de proteínas y su función en la biología.")

st.divider()

# --- TABS PRINCIPALES ---
t1, t2, t3, t4, t5, t6, t7 = st.tabs([
    "Proteínas", 
    "Proteínas Fibrosas", 
    "Proteínas Globulares", 
    "Proteínas de Membrana", 
    "Proteínas Motoras", 
    "Proteínas de Almacenamiento",
    "Proteínas Reguladoras"
])

# -----------------------------
# TAB 1: PROTEÍNAS (GENERAL)
# -----------------------------
with t1:
    st.header("🔬 Proteínas")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Protein_primary_structure.svg/1200px-Protein_primary_structure.svg.png",
             caption="Estructura primaria de una proteína", use_column_width=True)

    st.write("""
    Las proteínas son macromoléculas esenciales compuestas por aminoácidos enlazados entre sí. 
    Participan en una amplia variedad de procesos biológicos, como la estructura celular, la regulación metabólica, 
    el transporte de sustancias y la defensa del organismo. Su función depende directamente de la secuencia y 
    forma tridimensional de sus cadenas, lo que les permite adoptar múltiples roles indispensables para la vida.
    """)

# -----------------------------
# TAB 2: FIBROSAS
# -----------------------------
with t2:
    st.header("🧵 Proteínas Fibrosas")
    st.image("https://lh4.googleusercontent.com/proxy/sVYXyVjIRHaxr67QFx7PTXwxb5h6uhZzaiJGAM56w49uHBMYgASkb63uU6co7_kGxSLc4xfMPpzhzFHEb1M16OvgXZqMWgrDYQcgibEQgnPizFraDNf05hqvkGXgT-jf2e-dlsUsaXk_",
             caption="Fibras de colágeno", use_column_width=True)

    st.write("""
    Las proteínas fibrosas se caracterizan por presentar estructuras largas, alargadas y con forma de fibras. 
    Son altamente resistentes y desempeñan funciones principalmente estructurales, proporcionando soporte 
    y elasticidad a tejidos como la piel, músculos, tendones y cabello. Ejemplos importantes incluyen el 
    colágeno, la queratina y la elastina, que conforman gran parte del armazón del cuerpo.
    """)

# -----------------------------
# TAB 3: GLOBULARES
# -----------------------------
with t3:
    st.header("⚪ Proteínas Globulares")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/60/Myoglobin.png",
             caption="Mioglobina, una proteína globular clásica", use_column_width=True)

    st.write("""
    Las proteínas globulares tienen una estructura compacta y esférica que les permite participar 
    en procesos dinámicos dentro del organismo. Suelen ser solubles en agua y desempeñan funciones 
    como transporte, catálisis de reacciones químicas y regulación celular. Ejemplos de este tipo 
    son las enzimas, anticuerpos y hormonas proteicas, todas esenciales para mantener el equilibrio fisiológico.
    """)

# -----------------------------
# TAB 4: DE MEMBRANA
# -----------------------------
with t4:
    st.header("🧱 Proteínas de Membrana")
    st.image("https://cdn.kastatic.org/ka-perseus-images/232f4a59434cfe373a9a19fecfd7bd6e87dcb67f.png",
             caption="Proteínas integrales y periféricas en la membrana celular", use_column_width=True)

    st.write("""
    Las proteínas de membrana están incrustadas o asociadas a la membrana celular, donde cumplen funciones vitales 
    como el transporte de moléculas, la transmisión de señales y el mantenimiento de la estructura celular. 
    Pueden atravesar la membrana o ubicarse en su superficie interna o externa, permitiendo la comunicación 
    entre el interior de la célula y su entorno.
    """)

# -----------------------------
# TAB 5: MOTORAS
# -----------------------------
with t5:
    st.header("⚙️ Proteínas Motoras")
    st.image("https://images.my.labster.com/0972b7e9-8757-4ea6-b6de-382a1d15fe84/MUT_Contraction2.es_ES.png",
             caption="Miosina desplazándose sobre filamentos de actina", use_column_width=True)

    st.write("""
    Las proteínas motoras son responsables del movimiento dentro de las células y del desplazamiento 
    de estructuras completas como los músculos. Utilizan energía, normalmente en forma de ATP, para 
    generar cambios conformacionales que producen movimiento. Entre las más importantes se encuentran 
    la miosina, la quinesina y la dineína, esenciales para el transporte intracelular y la contracción muscular.
    """)

# -----------------------------
# TAB 6: ALMACENAMIENTO
# -----------------------------
with t6:
    st.header("📦 Proteínas de Almacenamiento")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmgvLCr-HSezbtxuhWZybdBSyJqAj6gyBqVQ&s",
             caption="Ferritina: proteína que almacena hierro", use_column_width=True)

    st.write("""
    Las proteínas de almacenamiento se encargan de acumular y conservar nutrientes, especialmente 
    aminoácidos y minerales esenciales, para ser utilizados posteriormente por el organismo o por 
    células en crecimiento. Ejemplos comunes son la ferritina, que almacena hierro en animales, 
    y las proteínas de reserva presentes en semillas como la gliadina o la zeína.
    """)

# -----------------------------
# TAB 7: REGULADORAS
# -----------------------------
with t7:
    st.header("🧭 Proteínas Reguladoras")
    st.image("https://cdn.lecturio.com/assets/Lac-operon-scaled.jpg",
             caption="Factores de transcripción regulando genes", use_column_width=True)

    st.write("""
    Las proteínas reguladoras participan en el control y coordinación de procesos biológicos. 
    Actúan activando o inhibiendo funciones específicas, regulando la expresión génica, modulando 
    rutas metabólicas o controlando el ciclo celular. Entre estas proteínas se encuentran los 
    factores de transcripción, algunas hormonas y proteínas que responden a señales del ambiente.
    """)
