import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Panel Estudiante", page_icon="👨‍🎓")

st.title(" Panel del Estudiante")
st.write("Aquí puedes buscar y reservar tus tutorías.")
st.divider()

# Buscar tutorías
st.subheader(" Buscar Tutoría")
col1, col2 = st.columns(2)

with col1:
    materia = st.selectbox("Materia", ["Cálculo", "Física", "Programación en Python", "Bases de Datos"])
with col2:
    fecha = st.date_input("Fecha preferida", min_value=date.today())

# Tabla de horarios disponibles (Datos falsos para el pitch)
st.write(f"Horarios disponibles para **{materia}**:")
datos = pd.DataFrame({
    "Docente": ["Ing. Carlos Gómez", "Dra. Ana Silva"],
    "Hora": ["10:00 AM", "02:00 PM"],
    "Modalidad": ["Presencial (Sala 3)", "Virtual (Meet)"]
})
st.dataframe(datos, use_container_width=True, hide_index=True)

# Formulario de Reserva
st.subheader("📅 Confirmar Reserva")
with st.form("form_reserva"):
    docente = st.selectbox("Selecciona el Docente", ["Ing. Carlos Gómez", "Dra. Ana Silva"])
    dudas = st.text_area("¿Qué temas específicos quieres tratar? (Opcional)")
    
    if st.form_submit_button("Reservar Tutoría"):
        if dudas.strip() == "": 
            st.warning("Sería útil escribir tus dudas, aunque sea breve.")
        st.success("¡Tutoría reservada con éxito!")
        st.balloons() 