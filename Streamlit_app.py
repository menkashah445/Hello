import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.write('Hello, *World!* :sunglasses:')
st.balloons()




arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
