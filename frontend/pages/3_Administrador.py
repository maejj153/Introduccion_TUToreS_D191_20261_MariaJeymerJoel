import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Panel Admin", page_icon="⚙️", layout="wide")

# Banner superior sobrio
st.markdown(
    """
    <div style='background-color:#1E3A8A; padding:25px; border-radius:8px;'>
        <h1 style='text-align:center; color:white; margin:0;'>Panel de Administración</h1>
        <p style='text-align:center; color:#CBD5E1; font-size:18px; margin:0;'>
            Vista general del Unisistema de Tutorías
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Sección 1: Métricas clave
st.markdown("<h2 style='color:#1E3A8A;'>Estadísticas Generales</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.metric(label="Estudiantes Registrados", value="150", delta="+12 este mes")
col2.metric(label="Docentes Activos", value="24", delta="+2 este mes")
col3.metric(label="Tutorías Realizadas", value="320", delta="85% completadas")

st.divider()

# Layout en dos columnas principales
col_izq, col_der = st.columns([3,1])

# Columna izquierda: Gestión de Usuarios
with col_izq:
    st.markdown("<h2 style='color:#1E3A8A;'>Gestión de Usuarios</h2>", unsafe_allow_html=True)
    rol_filtro = st.radio("Selecciona qué usuarios ver:", ["Estudiantes", "Docentes"], horizontal=True)

    if rol_filtro == "Estudiantes":
        usuarios = pd.DataFrame({
            "ID": ["E001", "E002", "E003"],
            "Nombre": ["Ana Silva", "Luis Gómez", "Carlos Ruiz"],
            "Carrera": ["Ing. Sistemas", "Ing. Industrial", "Ing. Sistemas"],
            "Estado": ["Activo", "Activo", "Inactivo"]
        })
    else:
        usuarios = pd.DataFrame({
            "ID": ["D001", "D002"],
            "Nombre": ["Ing. Carlos Gómez", "Dra. Ana Silva"],
            "Departamento": ["Matemáticas", "Física"],
            "Estado": ["Activo", "Activo"]
        })

    st.dataframe(usuarios, use_container_width=True, hide_index=True)

# Columna derecha: Acción de exportar
with col_der:
    st.markdown("<h2 style='color:#1E3A8A;'>Acciones</h2>", unsafe_allow_html=True)
    if st.button("Exportar Reporte a Excel", use_container_width=True):
        st.info("Generando reporte... (Función simulada para el prototipo visual)")
