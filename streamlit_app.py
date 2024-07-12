import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuración del tema
st.set_page_config(
    page_title="Circunferencia",
    page_icon=":circumference:",
    layout="wide",
    initial_sidebar_state="expanded",
   theme={
        primaryColor #6eb52f,
        backgroundColor #f0f0f5,
        secondaryBackgroundColor #e0e0ef,
        textColor #262730,
        font sans serif,
    }
)

# Introducción
st.title("Circunferencia")
st.write("Bienvenido a la aplicación de circunferencia!")

# Ecuación y fundamentación matemática
st.header("Ecuación y fundamentación matemática")
st.write("La ecuación de la circunferencia es:")
st.latex(r"((x-h)^2 + (y-k)^2 = r^2)")
st.write("Donde (h, k) es el centro de la circunferencia y r es el radio.")

# Componente interactivo para el usuario
st.header("Ingrese las coordenadas x e y de la circunferencia")
x = st.number_input("Ingrese x:", value=0)
y = st.number_input("Ingrese y:", value=0)
r = st.number_input("Ingrese el radio:", value=1)

# Gráfica con cuadricula
st.header("Gráfica de la circunferencia")
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.grid(True)
ax.plot(x, y, "ro")
circle = plt.Circle((x, y), r, fill=False)
ax.add_artist(circle)
st.pyplot(fig)

# Explicación del funcionamiento del código
st.header("Explicación del funcionamiento del código")
st.write("Este código utiliza la biblioteca Streamlit para crear una aplicación interactiva que permite al usuario ingresar las coordenadas x e y de la circunferencia y el radio. Luego, utiliza la biblioteca Matplotlib para generar una gráfica de la circunferencia con cuadricula.")
st.write("La ecuación de la circunferencia se utiliza para calcular los puntos de la circunferencia y se grafican utilizando la función `plot` de Matplotlib.")
st.write("La aplicación también incluye un componente interactivo que permite al usuario ingresar los valores de x, y y r utilizando cajas de entrada.")

# Despliegue online
st.write("Puedes desplegar esta aplicación online utilizando Streamlit Sharing.")


