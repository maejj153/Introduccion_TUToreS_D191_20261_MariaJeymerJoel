import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Sistema de Tutorías", page_icon="📚", layout="centered")

st.title("📚 Bienvenido al sistema de Tutorías UTS")
st.write("Selecciona tu rol en el menú lateral para navegar.")

# Simulador de Login
st.subheader("Ingreso al Sistema")
rol = st.selectbox("¿Qué rol tienes?", ["Estudiante", "Docente", "Administrador"])
email = st.text_input("Correo Institucional")
password = st.text_input("Contraseña", type="password")

if st.button("Ingresar"):
    st.success(f"¡Login exitoso! Bienvenido/a. Dirígete a tu panel en la barra lateral.")