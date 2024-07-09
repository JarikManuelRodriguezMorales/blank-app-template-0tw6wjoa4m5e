import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Introducción al tema
st.title("Circunferencia de un Círculo")
st.write("La circunferencia de un círculo es la distancia alrededor del círculo. Es un concepto fundamental en matemáticas y se utiliza en muchas aplicaciones del mundo real.")

# Fundamentación matemática
st.write("La ecuación de la circunferencia de un círculo es:")
st.latex(r"(x-h)^2 + (y-k)^2 = r^2")
st.write("Donde (h, k) es el centro del círculo y r es el radio del círculo.")

# Componente interactivo
st.write("Ingrese los valores del centro del círculo (h, k) y el radio (r):")
h = st.slider("h", -10, 10, 0)
k = st.slider("k", -10, 10, 0)
r = st.slider("r", 0, 10, 5)

# Graficar el círculo
fig, ax = plt.subplots()
theta = np.linspace(0, 2*np.pi, 100)
x = h + r * np.cos(theta)
y = k + r * np.sin(theta)
ax.plot(x, y)
ax.set_xlim(h-10, h+10)
ax.set_ylim(k-10, k+10)
ax.set_aspect('equal')
st.pyplot(fig)

# Desplegar la app online
# Puedes desplegar la app en GitHub Pages o otras plataformas que soporten apps de Streamlit.

