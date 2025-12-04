import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN VISUAL ---
st.set_page_config(
    page_title="BioProteínas | Enciclopedia de Proteínas",
    layout="wide",
    page_icon="🧬"
)

st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        border: 1px solid rgba(150, 150, 150, 0.2);
        color: inherit;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(100, 100, 100, 0.1);
        border-bottom: 2px solid #FF4B4B;
        font-weight: bold;
    }
    .definition-box {
        padding: 20px;
        border-left: 5px solid #FF4B4B;
        background-color: rgba(128, 128, 128, 0.1);
        margin-bottom: 20px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🧬 Enciclopedia Visual de Proteínas")
st.markdown("Explora la biología molecular: estructura, función y relevancia biomédica.")


# --- TABS PRINCIPALES ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔬 ¿Qué son las proteínas?",
    "⚙️ Funciones",
    "🧱 Estructura",
    "📚 Clasificación",
    "🧪 Ejemplos importantes",
    "🏥 Importancia biomédica"
])

# -------------------------------------------------------------------
# TAB 1 — ¿QUÉ SON LAS PROTEÍNAS?
# -------------------------------------------------------------------
with tab1:
    st.header("🔬 ¿Qué son las proteínas?")
    st.markdown("""
    Las **proteínas** son macromoléculas esenciales formadas por cadenas de aminoácidos unidas mediante enlaces peptídicos.
    Constituyen uno de los principales componentes de todas las células y participan en prácticamente todos los procesos biológicos.

    ### 🌟 Características principales
    - Están formadas por **20 aminoácidos** distintos.
    - Adquieren una estructura tridimensional específica.
    - Determinan funciones como catálisis, transporte y señalización celular.
    - Pueden ser muy pequeñas o gigantes (miles de aminoácidos).
    """)

    st.markdown("""
    ### 🧬 ¿Por qué son importantes?
    Las proteínas son **la maquinaria de la vida**. Nada en una célula funciona correctamente sin proteínas:
    - No habría metabolismo sin enzimas.
    - No habría musculatura sin actina ni miosina.
    - No habría sistema inmune sin anticuerpos.
    """)


# -------------------------------------------------------------------
# TAB 2 — FUNCIONES
# -------------------------------------------------------------------
with tab2:
    st.header("⚙️ Funciones de las proteínas")

    st.markdown("""
    Las proteínas desempeñan funciones vitales en todos los organismos vivos. Algunas de las más importantes incluyen:
    """)

    funciones = {
        "Enzimática": "Catalizan reacciones químicas (ej. amilasa, ADN polimerasa).",
        "Estructural": "Forman parte de tejidos (colágeno, queratina).",
        "Transporte": "Transportan moléculas (hemoglobina).",
        "Defensa": "Participan en la respuesta inmune (anticuerpos).",
        "Regulación": "Controlan procesos celulares (hormonas proteicas).",
        "Movimiento": "Permiten la contracción muscular (actina y miosina).",
        "Almacenamiento": "Reservan aminoácidos o iones (ferritina)."
    }

    df_funciones = pd.DataFrame({
        "Función": list(funciones.keys()),
        "Descripción": list(funciones.values())
    })

    st.dataframe(df_funciones, use_container_width=True)


# -------------------------------------------------------------------
# TAB 3 — ESTRUCTURA
# -------------------------------------------------------------------
with tab3:
    st.header("🧱 Niveles estructurales de las proteínas")

    st.markdown("""
    Las proteínas adquieren su función gracias a su **estructura**, que se organiza en cuatro niveles:
    """)

    st.subheader("1️⃣ Estructura primaria")
    st.markdown("Secuencia lineal de aminoácidos unidos por enlaces peptídicos.")

    st.subheader("2️⃣ Estructura secundaria")
    st.markdown("Patrones locales como **hélice alfa** y **lámina beta** formados por puentes de hidrógeno.")

    st.subheader("3️⃣ Estructura terciaria")
    st.markdown("Plegamiento tridimensional completo de la proteína debido a interacciones débiles.")

    st.subheader("4️⃣ Estructura cuaternaria")
    st.markdown("Asociación de varias cadenas polipeptídicas (como en la hemoglobina).")

    st.info("La forma determina la función. Un cambio estructural = pérdida de función → enfermedades.")


# -------------------------------------------------------------------
# TAB 4 — CLASIFICACIÓN
# -------------------------------------------------------------------
with tab4:
    st.header("📚 Clasificación de proteínas")

    st.markdown("""
    Las proteínas se pueden clasificar según diversos criterios:
    """)

    st.subheader("📌 Por forma")
    st.markdown("- **Fibrosas** (colágeno)\n- **Globulares** (enzimas, anticuerpos)")

    st.subheader("📌 Por composición")
    st.markdown("- **Simples**: solo aminoácidos\n- **Conjugadas**: poseen grupos no proteicos")

    st.subheader("📌 Por función")
    st.markdown("- Enzimáticas, estructurales, transportadoras, hormonales, señalización, movimiento…")


# -------------------------------------------------------------------
# TAB 5 — EJEMPLOS IMPORTANTES
# -------------------------------------------------------------------
with tab5:
    st.header("🧪 Ejemplos relevantes de proteínas")

    ejemplos = {
        "Hemoglobina": "Transporta oxígeno en la sangre.",
        "Actina": "Participa en el movimiento celular.",
        "Colágeno": "Da resistencia a la piel, tendones y huesos.",
        "Insulina": "Regula los niveles de glucosa.",
        "Inmunoglobulinas": "Defensa contra patógenos.",
        "ADN polimerasa": "Replica el ADN durante la división celular."
    }

    df_ej = pd.DataFrame({
        "Proteína": ejemplos.keys(),
        "Función": ejemplos.values()
    })

    st.table(df_ej)


# -------------------------------------------------------------------
# TAB 6 — IMPORTANCIA BIOMÉDICA
# -------------------------------------------------------------------
with tab6:
    st.header("🏥 Importancia biomédica de las proteínas")

    st.markdown("""
    Las proteínas son fundamentales para la medicina moderna:

    ### 🧬 Diagnóstico
    - Biomarcadores en suero (troponinas, PCR, ferritina).
    - Anticuerpos utilizados en pruebas rápidas.

    ### 🧫 Tratamientos
    - Terapias basadas en anticuerpos monoclonales.
    - Enzimas terapéuticas.
    - Hormonas recombinantes.

    ### 🧪 Ingeniería biomédica
    - Diseño de proteínas para mejorar fármacos.
    - Ingeniería de anticuerpos para cáncer.
    - Producción recombinante en bacterias y levaduras.

    ### 🧠 Enfermedades relacionadas
    - Alzheimer (proteínas mal plegadas).
    - Fibrosis quística.
    - Hemoglobinopatías.
    """)

    st.success("Las proteínas son la base del diagnóstico, tratamiento y prevención de enfermedades modernas.")
