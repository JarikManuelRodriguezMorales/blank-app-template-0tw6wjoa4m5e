import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Introduction to the topic
st.title("Circumference of a Circle")
st.write("The circumference of a circle is the distance around the circle. It is a fundamental concept in mathematics and is used in many real-world applications.")

# Mathematical foundation
st.write("The formula to calculate the circumference of a circle is:")
st.latex(r"C = 2 \pi r")
st.write("Where C is the circumference, π is a mathematical constant approximately equal to 3.14, and r is the radius of the circle.")

# Interactive component
st.write("Enter the radius of the circle:")
radius = st.slider("Radius", 0.0, 10.0, 1.0)

# Calculate the circumference
circumference = 2 * np.pi * radius

# Display the result
st.write("The circumference of the circle is:")
st.write(circumference)

# Plot the circle
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), radius, fill=False)
ax.add_artist(circle)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
st.pyplot(fig)

# Deploy the app online
# You can deploy the app on GitHub Pages or other platforms that support Streamlit apps.
