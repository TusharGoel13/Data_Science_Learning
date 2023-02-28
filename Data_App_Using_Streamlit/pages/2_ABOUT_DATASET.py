import streamlit as st
from matplotlib import image
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "lter_penguins1.jpg")

st.set_page_config(page_title='About Palmer Penguin Dataset')
st.title(":blue[Palmer Archipelago (Antarctica) Penguin Dataset]")

img = image.imread(IMAGE_PATH)
st.image(img)


st.header(":red[Dataset]")
st.markdown('''**The palmerpenguins data contains size measurements for three penguin species observed on three islands in the Palmer Archipelago, Antarctica.
           This data were collected from 2007 - 2009 by Dr. Kristen Gorman with the Palmer Station Long Term Ecological Research Program, part of the US Long Term Ecological Research Network.**''')
st.markdown("**This dataset contains 8 variables with total observations of 344 penguins :penguin:**")
st.markdown("**Aside: That’s right, developers – Gentoo Linux is named after penguins!**")


st.header(":orange[Attributes]")
st.markdown(":snowman_without_snow: **SPECIES: Chinstrap, Adélie, or Gentoo**")
st.markdown(":snowman_without_snow: **ISLAND: Dream, Torgersen, or Biscoe in the Palmer Archipelago (Antarctica)**")
st.markdown(":snowman_without_snow: **CULMEN LENGTH: The length of the upper ridge of a bird's beak (mm)**")
st.markdown(":snowman_without_snow: **CULMEN DEPTH: The depth of the upper ridge of a bird's beak (mm)**")
st.markdown(":snowman_without_snow: **FLIPPER LENGTH: The length of  flat broad limb or wings used for swimming (mm)**")
st.markdown(":snowman_without_snow: **BODY MASS: body mass (grams)**")
st.markdown(":snowman_without_snow: **SEX: Male oe Female**")
