import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Sistema de Tutorías", page_icon="📚", layout="centered")

# Inicializar session_state
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "rol" not in st.session_state:
    st.session_state.rol = None

# --- Usuarios simulados (en un sistema real vendrían de una base de datos) ---
USUARIOS = {
    "estudiante@uts.edu.co": {"password": "est123", "rol": "Estudiante"},
    "docente@uts.edu.co":    {"password": "doc123", "rol": "Docente"},
    "admin@uts.edu.co":      {"password": "adm123", "rol": "Administrador"},
}

# --- Si ya está autenticado, mostrar bienvenida ---
if st.session_state.autenticado:
    st.title("📚 Sistema de Tutorías UTS")
    st.success(f"✅ Sesión iniciada como **{st.session_state.rol}**")
    st.info("👈 Usa el menú lateral para navegar a tu panel.")

    if st.button("Cerrar sesión"):
        st.session_state.autenticado = False
        st.session_state.rol = None
        st.rerun()

# --- Si NO está autenticado, mostrar login ---
else:
    st.title("📚 Bienvenido al Sistema de Tutorías UTS")
    st.subheader("Ingreso al Sistema")

    email = st.text_input("Correo Institucional")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if email in USUARIOS and USUARIOS[email]["password"] == password:
            st.session_state.autenticado = True
            st.session_state.rol = USUARIOS[email]["rol"]
            st.rerun()
        else:
            st.error("❌ Correo o contraseña incorrectos.")
