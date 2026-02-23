import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Panel Docente", page_icon="👨‍🏫", layout="wide")

# --- Protección de acceso ---
if not st.session_state.get("autenticado"):
    st.error("🔒 Debes iniciar sesión para acceder a esta página.")
    st.page_link("main.py", label="Ir al Login", icon="🔑")
    st.stop()

if st.session_state.get("rol") != "Docente":
    st.error("⛔ No tienes permiso para acceder a esta página.")
    st.stop()

# --- Botón cerrar sesión en barra lateral ---
with st.sidebar:
    st.markdown(f"👤 **{st.session_state.rol}**")
    st.divider()
    if st.button("🚪 Cerrar Sesión", use_container_width=True):
        st.session_state.autenticado = False
        st.session_state.rol = None
        st.switch_page("main.py")

# --- Contenido del panel ---
st.markdown(
    """
    <div style='background-color:#1E3A8A; padding:25px; border-radius:8px;'>
        <h1 style='text-align:center; color:white; margin:0;'>Panel del Docente</h1>
        <p style='text-align:center; color:#CBD5E1; font-size:18px; margin:0;'>
            Bienvenido, Ing. Carlos Gómez. Gestiona tus horarios y solicitudes
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

col_izq, col_der = st.columns([2, 1])

with col_izq:
    st.markdown("<h2 style='color:#1E3A8A;'>Mis Próximas Tutorías</h2>", unsafe_allow_html=True)
    tutorias = pd.DataFrame({
        "Estudiante": ["María López", "Juan Pérez"],
        "Materia": ["Cálculo", "Física"],
        "Fecha": ["2026-02-25", "2026-02-26"],
        "Hora": ["10:00 AM", "02:00 PM"],
        "Estado": ["Confirmada", "Pendiente"]
    })
    st.dataframe(tutorias, use_container_width=True, hide_index=True)

with col_der:
    st.markdown("<h2 style='color:#1E3A8A;'>Publicar Nuevo Horario</h2>", unsafe_allow_html=True)
    with st.form("form_horario"):
        fecha = st.date_input("Fecha disponible", min_value=datetime.date.today())
        hora = st.time_input("Hora de inicio")
        modalidad = st.selectbox("Modalidad", ["Presencial (Oficina)", "Virtual (Meet/Zoom)"])
        enlace = st.text_input("Enlace o Lugar (Ej: Sala 4)")

        if st.form_submit_button("Publicar Horario", use_container_width=True):
            st.success("¡Horario publicado correctamente! Los estudiantes ya pueden verlo.")
