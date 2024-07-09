import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Introducción al tema
st.title("Circunferencia de un Círculo")
st.write("La circunferencia de un círculo es la distancia alrededor del círculo. Es un concepto fundamental en matemáticas y se utiliza en muchas aplicaciones del mundo real.")

# Fundamentación matemática
st.write("La fórmula para calcular la circunferencia de un círculo es:")
st.latex(r"C = 2 \pi r")
st.write("Donde C es la circunferencia, π es una constante matemática aproximadamente igual a 3.14, y r es el radio del círculo.")

# Componente interactivo
st.write("Ingrese el radio del círculo:")
radio = st.slider("Radio", 0.0, 10.0, 1.0)

# Calcular la circunferencia
circunferencia = 2 * np.pi * radio

# Mostrar el resultado
st.write("La circunferencia del círculo es:")
st.write(circunferencia)

# Graficar el círculo
fig, ax = plt.subplots()
circulo = plt.Circle((0, 0), radio, fill=False)
ax.add_artist(circulo)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
st.pyplot(fig)

