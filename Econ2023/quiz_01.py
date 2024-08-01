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

# ## Fir use background image from directory and later from a plot object:
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


# # def process_canvas():
# #     st.write("Hi")


# # # Convert the matplotlib figure to a PIL Image
# # buf = io.BytesIO()
# # plt.savefig(buf, format='png')
# # buf.seek(0)
# # bg_image = Image.open(buf)

# Open the image
bg_image = Image.open("Econ2023/bg_image.png")
scaleFactors = [100, 100, .1214, .775]


def process_canvas():
    canvas_width = 600
    canvas_height = 500

    # Specify canvas parameters in application
    drawing_mode = st.sidebar.selectbox(
        "Drawing tool:", (
            "line",
            "point",
            "rect",
            "polygon",
            "transform"
        )
    )

    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider(
            "Point display radius: ", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Stroke color hex: ")

    realtime_update = st.sidebar.checkbox("Update in realtime", True)

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_image=bg_image,
        update_streamlit=realtime_update,
        width=canvas_width,
        height=canvas_height,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        scaleFactors=scaleFactors,
        key="canvas",
    )

    if canvas_result.image_data is not None:

        img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')

        # Resize the user-drawn image to match the size of the background image
        img = img.resize(bg_image.size)
        # Combine the user-drawn image and the background image
        combined = Image.alpha_composite(bg_image.convert('RGBA'), img)

        # Save the combined image to a BytesIO object
        combined_io = io.BytesIO()
        combined.save(combined_io, 'PNG')
        combined_io.seek(0)

        # Convert the combined image to a base64 encoded string to be saved to database or template
        base64_combined = base64.b64encode(combined_io.getvalue()).decode()

        # # Create a download button for the image
        st.download_button(
            label="Download-canvas-image",
            # data=img_io,
            data=combined_io,
            file_name='image01.png',
            mime='image/png'
        )
        return base64_combined


process_canvas()
