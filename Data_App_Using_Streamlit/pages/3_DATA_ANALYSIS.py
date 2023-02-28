import streamlit as st
from matplotlib import image
import pandas as pd
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "penguins_size.csv")

st.set_page_config(page_title='Palmer Penguin Data Analysis')

st.header(":violet[DataFrame]")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)



st.header(":red[Details of the Dataset]")
st.markdown("**Select on sidebar to view the details:**")
section = st.sidebar.radio('Select a section to view', ['Head', 'Tail', 'Columns', 'Shape', 'Descriptive Statistics', 'Missing Values'])

# Display the first few rows of the dataset
if section == 'Head':
    st.subheader('First 5 rows')
    st.write(df.head())

# Display the last few rows of the dataset
elif section == 'Tail':
    st.subheader('Last 5 rows')
    st.write(df.tail())

# Display the columns of the dataset
elif section == 'Columns':
    st.subheader('Columns')
    st.write(df.columns)

# Display the shape of the dataset
elif section == 'Shape':
    st.subheader('Shape')
    st.write(df.shape)
    
# Display descriptive statistics for each variable
elif section == 'Descriptive Statistics':
    st.subheader('Descriptive Statistics')
    st.write(df.describe())

# Display missing values
elif section == 'Missing Values':
    st.subheader('Missing Values')
    st.write(df.isnull().sum())

st.header(":orange[Filtered Dataset]")
# Create a sidebar with dropdown menus to select a penguin species and an island
species = st.selectbox("Select a penguin species:", df['species'].unique())
island = st.selectbox("Select an island:", df['island'].unique())

# Filter the dataset based on the selected species and island
filtered_df = df[(df['species'] == species) & (df['island'] == island)]

# Display the filtered data
st.write(filtered_df)
