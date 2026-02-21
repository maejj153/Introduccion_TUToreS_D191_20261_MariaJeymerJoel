import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Panel Docente", page_icon="👨‍🏫")

st.title("👨‍🏫 Panel del Docente")
st.write("Bienvenido, **Ing. Carlos Gómez**. Aquí puedes gestionar tus horarios y solicitudes.")
st.divider()

# Sección 1: Próximas tutorías (Simuladas)
st.subheader("📌 Mis Próximas Tutorías")
tutorias = pd.DataFrame({
    "Estudiante": ["María López", "Juan Pérez"],
    "Materia": ["Cálculo", "Física"],
    "Fecha": ["2026-02-25", "2026-02-26"],
    "Hora": ["10:00 AM", "02:00 PM"],
    "Estado": ["Confirmada", "Pendiente"]
})
# Mostramos la tabla de forma limpia
st.dataframe(tutorias, use_container_width=True, hide_index=True)

# Sección 2: Agregar nueva disponibilidad
st.subheader("➕ Publicar Nuevo Horario")
with st.form("form_horario"):
    col1, col2 = st.columns(2)
    
    with col1:
        fecha = st.date_input("Fecha disponible", min_value=datetime.date.today())
        hora = st.time_input("Hora de inicio")
        
    with col2:
        modalidad = st.selectbox("Modalidad", ["Presencial (Oficina)", "Virtual (Meet/Zoom)"])
        enlace = st.text_input("Enlace o Lugar (Ej: Sala 4)")

    # Botón para enviar el formulario
    if st.form_submit_button("Publicar Horario"):
        st.success("¡Horario publicado correctamente! Los estudiantes ya pueden verlo.")