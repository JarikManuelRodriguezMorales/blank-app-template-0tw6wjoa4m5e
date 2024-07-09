import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Introducción al tema
st.title("La Ecuación de la Circunferencia")
st.write("La ecuación de la circunferencia es una de las ecuaciones más importantes en matemáticas, y se utiliza para describir la forma de un círculo en un plano cartesiano.")

# Explicación de la ecuación
st.write("La ecuación de la circunferencia se puede escribir como:")
st.latex(r"(x-h)^2 + (y-k)^2 = r^2")
st.write("Donde:")
st.write("* (h, k) es el centro del círculo")
st.write("* r es el radio del círculo")
st.write("* x e y son las coordenadas de un punto en el plano cartesiano")

# Desarrollo de la ecuación
st.write("Para entender cómo se desarrolla la ecuación, podemos empezar por considerar un punto (x, y) en el plano cartesiano.")
st.write("La distancia entre el punto (x, y) y el centro del círculo (h, k) se puede calcular utilizando la fórmula de la distancia entre dos puntos:")
st.latex(r"d = \sqrt{(x-h)^2 + (y-k)^2}")
st.write("Si el punto (x, y) se encuentra en la circunferencia, entonces la distancia entre el punto y el centro del círculo es igual al radio del círculo:")
st.latex(r"d = r")
st.write("Sustituyendo la fórmula de la distancia en la ecuación anterior, obtenemos la ecuación de la circunferencia:")
st.latex(r"(x-h)^2 + (y-k)^2 = r^2")

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
