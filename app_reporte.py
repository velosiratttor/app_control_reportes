import streamlit as st
import pandas as pd
from openpyxl import load_workbook


ruta='reporte.xlsx'
df.conver_excel(ruta,index=False)

st.title("registro de actividades diarias")
st.write("app de registro de actividades")

if "datos" not in st.session_state:
    st.session_state.datos=[]


nombre= st.text_input("Nombre del analista")
fecha=st.date_input("fecha de la actividad")
actividad=st.selectbox(
    "Seleccione su actividad",
    ["AUTORIZACIÓN PARA EL INGRESO DE CALIFICACIONES (AÑOS ANTERIORES)",
     "REENVIO DE CERTIFICADOS DE CURSOS VIRTUALES",
     "CORRECIÓN DE DATOS DE ESTUDIANTE/PROTAGONISTA",
     "ASISTENCIA VIA TELEFONICA A C.T.",
     "SOLICITUD PARA CAMBIO DE CORREO"],
     index=None,
     placeholder="Debes seleccionar tus acticvidades realizadas",
     accept_new_options=True,
)
estado=st.selectbox(
    "Estado de la actividad",
    ["ATENDIDO",
     "EN ATENCION",
     "ESCLADO"],
     index=None,
     placeholder="seleccione el estado de tu actividad",
     accept_new_options=True,
)


if st.button("agregar"):
    st.session_state.datos.append({
        "Nombre":nombre,
        "Fecha":fecha,
        "Actividad":actividad,
        "Estado":estado
    })

df= pd.DataFrame(st.session_state.datos)
st.dataframe(df)

#st.write("Nombre",nombre)
#st.write("Fecha",fecha)
#st.write("Actividad",actividad)
#st.write("Estado",estado)