import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, UnidentifiedImageError
import io
import os
# import pandas as pd  # pip install pandas
import numpy as np  # pip install numpy
from PIL import Image  # pip install pillow
import streamlit as st  # pip install streamlit
# pip install streamlit-drawable-canvas # to install from pypi
from streamlit_drawable_canvas import st_canvas
import base64
import seaborn as sns  # pip install seaborn
import matplotlib.pyplot as plt  # pip install matplotlib
from fn_drawables import process_canvas

# # Fir use background image from directory and later from a plot object:
# x_lim = [0, 100]
# y_lim = [0, 100]

# xsteps = (x_lim[1]-x_lim[0])/10
# ysteps = (y_lim[1]-y_lim[0])/10

# # constant that are mentioned in
# scaleFactors = [x_lim[1], y_lim[1], .1214, .775]

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Set the limits of the plot
# ax.set_xlim([x_lim[0], x_lim[1]])
# ax.set_ylim([y_lim[0], y_lim[1]])

# # Set the labels of the plot
# ax.set_xlabel('Quantity, Q')
# ax.set_ylabel('Price, P')

# # Specify the locations of the grid lines
# x_ticks = np.arange(x_lim[0], x_lim[1] + 1, xsteps)
# # Grid lines from 0 to 10 with a step of z
# y_ticks = np.arange(y_lim[0], y_lim[1] + 1, ysteps)

# ax.set_xticks(x_ticks)
# ax.set_yticks(y_ticks)

# # Draw a grid
# ax.grid(True)

# # Use streamlit to display the plot
# # st.pyplot(fig)


# # Convert the matplotlib figure to a PIL Image
# buf = io.BytesIO()
# plt.savefig(buf, format='png')
# buf.seek(0)
# bg_image = Image.open(buf)

# Debug: Check if the image is loaded correctly
# st.image(bg_image, caption="Background Image")

# Open and use image from folder
bg_image = Image.open("images/bg_image.png")
# bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
# st.image(bg_image, caption="Background Image")
scaleFactors = [100, 100, .1214, .775]

process_canvas(bg_image, scaleFactors)
