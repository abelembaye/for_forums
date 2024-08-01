import streamlit as st
import numpy as np
from PIL import Image
import numpy as np  # pip install numpy
import streamlit as st  # pip install streamlit
# pip install streamlit-drawable-canvas # to install from pypi
from streamlit_drawable_canvas import st_canvas
# from fn_drawables import process_canvas
from helper_fns import image_creation, process_canvas


# Call the function and use the returned image
bg_image = image_creation()

# Debug: Check if the image is loaded correctly and workking
st.write("Check if the image is loaded correctly and workking:")
st.image(bg_image, caption="Background Image")

# As alternative, open and use image from folder
# if 'bg_image' not in st.session_state:
#     st.session_state.bg_image = Image.open("images/bg_image.png")

# bg_image = st.session_state.bg_image

# bg_image = Image.open("images/bg_image.png")
# st.image(bg_image, caption="Background Image")

process_canvas(bg_image)
