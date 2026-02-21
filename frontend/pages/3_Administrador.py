import streamlit as st
import pandas as pd

st.set_page_config(page_title="Panel Admin", page_icon="⚙️")

st.title("⚙️ Panel de Administración")
st.write("Vista general del Unisistema de Tutorías.")
st.divider()

# Sección 1: Métricas clave (¡Esto se ve genial en un Pitch!)
st.subheader("📊 Estadísticas Generales")
col1, col2, col3 = st.columns(3)
col1.metric(label="Estudiantes Registrados", value="150", delta="+12 este mes")
col2.metric(label="Docentes Activos", value="24", delta="+2 este mes")
col3.metric(label="Tutorías Realizadas", value="320", delta="85% completadas")

st.divider()

# Sección 2: Gestión de Usuarios
st.subheader("👥 Gestión de Usuarios")
# Un botón de opción para alternar entre ver estudiantes o docentes
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

# Botón de acción simulada
if st.button("📥 Exportar Reporte a Excel"):
    st.info("Generando reporte... (Esta es una función simulada para el prototipo visual)")