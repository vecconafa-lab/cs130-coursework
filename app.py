import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# LABORATORIO 13 - ACTIVIDAD 3 (PARTE A)
# Caso: Plataforma Inteligente de Gestión de Citas Médicas
# Hospital de Lima Norte
# ============================================================

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Gestión de Citas Médicas",
    page_icon="🏥",
    layout="wide"
)

# ============================================================
# PALETA DE COLORES
# ============================================================

CREMA = "#F5F1E8"
BLANCO = "#FFFCF7"
NEGRO = "#292621"
MARRON = "#795C46"
VERDE = "#244C3A"
VERDE_CLARO = "#6E8B76"
BEIGE = "#D9CBB8"
GRIS = "#817A70"

# ============================================================
# ESTILOS CSS
# ============================================================

st.markdown("""
<style>

    /* Fondo principal */
    .stApp {
        background-color: #F5F1E8;
        color: #292621;
    }

    /* Área principal */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #292621 !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Texto */
    p, label, span {
        color: #292621;
    }

    /* Métricas */
    [data-testid="stMetric"] {
        background-color: #FFFCF7;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #D9CBB8;
    }

    /* Línea divisoria */
    hr {
        border-color: #D9CBB8;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# CARGAR DATASET
# ============================================================

try:
    df = pd.read_csv("citas_medicas.csv")
except FileNotFoundError:
    st.error("No se encontró el archivo 'citas_medicas.csv'.")
    st.stop()

# ============================================================
# ENCABEZADO
# ============================================================

st.title("🏥 Dashboard de Gestión de Citas Médicas")

st.caption(
    "Plataforma Inteligente de Gestión de Citas Médicas "
    "en un Hospital de Lima Norte"
)

st.markdown("---")

# ============================================================
# GRÁFICO 1: CITAS POR ESPECIALIDAD
# ============================================================

st.subheader("Citas por Especialidad")

fig1 = px.bar(
    df["especialidad"].value_counts().reset_index(),
    x="especialidad",
    y="count",
    labels={
        "count": "Cantidad de citas",
        "especialidad": "Especialidad"
    },
    title="Cantidad de citas por especialidad"
)

fig1.update_traces(
    marker_color=VERDE,
    marker_line_color=VERDE,
    marker_line_width=1,
    opacity=0.9
)

fig1.update_layout(
    plot_bgcolor=BLANCO,
    paper_bgcolor=BLANCO,
    font=dict(color=NEGRO),
    title_font=dict(color=NEGRO, size=18),
    xaxis=dict(
        title="Especialidad",
        showgrid=False
    ),
    yaxis=dict(
        title="Cantidad",
        gridcolor=BEIGE
    ),
    margin=dict(l=20, r=20, t=60, b=40)
)

st.plotly_chart(fig1, use_container_width=True)

# ============================================================
# GRÁFICO 2: ESTADO DE LAS CITAS
# ============================================================

st.subheader("Estado de las Citas")

fig2 = px.pie(
    df,
    names="estado",
    title="Distribución de estados de las citas",
    color_discrete_sequence=[
        VERDE,
        MARRON,
        VERDE_CLARO,
        BEIGE,
        "#A58B70"
    ]
)

fig2.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hole=0.45
)

fig2.update_layout(
    plot_bgcolor=BLANCO,
    paper_bgcolor=BLANCO,
    font=dict(color=NEGRO),
    title_font=dict(color=NEGRO, size=18),
    legend_title="Estado",
    margin=dict(l=20, r=20, t=60, b=40)
)

st.plotly_chart(fig2, use_container_width=True)

# ============================================================
# PREPARAR FECHAS
# ============================================================

df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month

# Agrupar citas por mes
citas_mes = df.groupby("mes").size().reset_index(name="cantidad")

# ============================================================
# GRÁFICO 3: CITAS POR MES
# ============================================================

st.subheader("Citas por Mes")

fig3 = px.line(
    citas_mes,
    x="mes",
    y="cantidad",
    markers=True,
    title="Cantidad de citas registradas por mes"
)

fig3.update_traces(
    line=dict(color=MARRON, width=4),
    marker=dict(
        color=VERDE,
        size=10,
        line=dict(color=BLANCO, width=2)
    )
)

fig3.update_layout(
    plot_bgcolor=BLANCO,
    paper_bgcolor=BLANCO,
    font=dict(color=NEGRO),
    title_font=dict(color=NEGRO, size=18),
    xaxis=dict(
        title="Mes",
        gridcolor=BEIGE
    ),
    yaxis=dict(
        title="Cantidad de citas",
        gridcolor=BEIGE
    ),
    margin=dict(l=20, r=20, t=60, b=40)
)

st.plotly_chart(fig3, use_container_width=True)

# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown("---")

st.caption(
    "Sistema de Gestión Inteligente de Citas Médicas | Hospital de Lima Norte"
)