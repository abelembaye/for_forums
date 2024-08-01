
import pandas as pd  # pip install pandas
import numpy as np  # pip install numpy
from PIL import Image  # pip install pillow
import streamlit as st  # pip install streamlit
# pip install streamlit-drawable-canvas # to install from pypi
from streamlit_drawable_canvas import st_canvas
import io
from io import BytesIO
import base64
import seaborn as sns  # pip install seaborn
import matplotlib.pyplot as plt  # pip install matplotlib


def process_canvas(bg_image, scaleFactors):
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
        background_image=bg_image,  # None,  # bg_image,
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
        # return base64_combined
