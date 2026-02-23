import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Panel Estudiante", page_icon="👨‍🎓", layout="wide")

# --- Protección de acceso ---
if not st.session_state.get("autenticado"):
    st.error("🔒 Debes iniciar sesión para acceder a esta página.")
    st.page_link("main.py", label="Ir al Login", icon="🔑")
    st.stop()

if st.session_state.get("rol") != "Estudiante":
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
        <h1 style='text-align:center; color:white; margin:0;'>Panel del Estudiante</h1>
        <p style='text-align:center; color:#CBD5E1; font-size:18px; margin:0;'>
            Gestiona tus tutorías de manera clara y organizada
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

col_izq, col_der = st.columns([2, 1])

with col_izq:
    st.markdown("<h2 style='color:#1E3A8A;'>Buscar Tutoría</h2>", unsafe_allow_html=True)
    materia = st.selectbox("Materia", ["Cálculo", "Física", "Programación en Python", "Bases de Datos"])
    fecha = st.date_input("Fecha preferida", min_value=date.today())

    st.markdown("<h2 style='color:#1E3A8A;'>Horarios disponibles</h2>", unsafe_allow_html=True)
    datos = pd.DataFrame({
        "Docente": ["Ing. Carlos Gómez", "Dra. Ana Silva"],
        "Hora": ["10:00 AM", "02:00 PM"],
        "Modalidad": ["Presencial (Sala 3)", "Virtual (Meet)"]
    })
    st.dataframe(datos, use_container_width=True, hide_index=True)

with col_der:
    st.markdown("<h2 style='color:#1E3A8A;'>Confirmar Reserva</h2>", unsafe_allow_html=True)
    with st.form("form_reserva"):
        docente = st.selectbox("Selecciona el Docente", ["Ing. Carlos Gómez", "Dra. Ana Silva"])
        dudas = st.text_area("Temas específicos a tratar (Opcional)", placeholder="Ejemplo: Integrales, circuitos eléctricos...")
        reservar = st.form_submit_button("Reservar Tutoría", use_container_width=True)
        if reservar:
            if dudas.strip() == "":
                st.warning("Sería útil escribir tus dudas, aunque sea breve.")
            st.success("¡Tutoría reservada con éxito!")
            st.snow()
