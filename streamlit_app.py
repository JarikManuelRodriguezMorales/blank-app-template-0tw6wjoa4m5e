import streamlit as st
import matplotlib.pyplot as plt

# Título y explicación
st.title("Ecuación de la circunferencia en el plano cartesiano")
st.write("En esta aplicación, podrás ingresar las coordenadas del centro `(a, b)` y el radio `r` de la ecuación `(x-a)² + (y-b)² = r²` y ver su gráfica correspondiente.")

# Entrada de datos
a = st.number_input("Ingresa la coordenada x del centro (a):", value=0.0, step=1.0)
b = st.number_input("Ingresa la coordenada y del centro (b):", value=0.0, step=1.0)
r = st.number_input("Ingresa el radio (r):", value=1.0, step=1.0)

# Explicación de la ecuación
st.write("La ecuación de la circunferencia en el plano cartesiano es:")
st.latex(r"(x - a)^2 + (y - b)^2 = r^2")
st.write("Donde:")
st.write("* `(x, y)` son las coordenadas de un punto en la circunferencia.")
st.write("* `(a, b)` son las coordenadas del centro de la circunferencia.")
st.write("* `r` es el radio de la circunferencia.")

# Gráfica interactiva
fig, ax = plt.subplots()
ax.grid(True, linestyle='--', color='gray', linewidth=0.5)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Gráfica de la circunferencia")
ax.plot([0, a], [0, b], color='red', linewidth=1.5, label="Centro")
ax.plot([a], [0], marker='o', color='red', markersize=5)
ax.plot([0], [b], marker='o', color='red', markersize=5)
ax.plot(a + r, b, marker='o', color='green', markersize=5, label="Punto en la circunferencia")
ax.plot(a - r, b, marker='o', color='green', markersize=5)
ax.legend()

# Generación de gráfica
if st.button("Generar gráfica"):
    plt.figure(figsize=(6, 6))
    plt.plot([a + r, a - r], [b, b], color='green', linewidth=1.5, label="Circunferencia")
    plt.plot([0, a], [0, b], color='red', linewidth=1.5, label="Centro")
    plt.plot([a], [0], marker='o', color='red', markersize=5)
    plt.plot([0], [b], marker='o', color='red', markersize=5)
    plt.plot(a + r, b, marker='o', color='green', markersize=5, label="Punto en la circunferencia")
    plt.plot(a - r, b, marker='o', color='green', markersize=5)
    plt.xlim(-r, r)
    plt.ylim(-r, r)
    plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Gráfica de la circunferencia")
    plt.legend()
    st.pyplot(plt)

# Footer
st.write("Desarrollado con ❤️ por [Tu nombre]")


