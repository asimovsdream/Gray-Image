import streamlit as st
from PIL import Image


upload_image = st.file_uploader("Browse Image")
with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert the pillow image to grayscale
    gray_img = img.convert("L")

    # render the grayscale image on the webpage
    st.image(gray_img)

    img.save("photo.png")

if upload_image:
    file = Image.open(upload_image)
    gray_file = file.convert("L")
    st.image(gray_file)