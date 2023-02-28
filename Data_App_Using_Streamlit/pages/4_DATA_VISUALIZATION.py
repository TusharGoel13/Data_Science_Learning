import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "penguins_size.csv")

st.set_page_config(page_title='Palmer Penguin Data Visualization')

df = pd.read_csv(DATA_PATH)

# Define a function to display a histogram of a given variable
def display_histogram(variable):
    fig, ax = plt.subplots()
    sns.histplot(data=df, x=df[variable], ax=ax, kde=True, hue='species', binwidth=3)
    ax.set_xlabel(variable.capitalize())
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Define a function to display a scatterplot of two given variables
def display_scatterplot(x_variable, y_variable):
    fig, ax = plt.subplots()
    sns.scatterplot(x=x_variable, y=y_variable, hue='species', data=df, ax=ax, palette="deep")
    ax.set_xlabel(x_variable.capitalize())
    ax.set_ylabel(y_variable.capitalize())
    st.pyplot(fig)

# Define a function to display a piechart of one given variables
def display_piechart(variable):
    fig, ax = plt.subplots()
    sizes = df[variable].value_counts()
    ax.pie(sizes, labels=sizes.index, autopct='%1.1f%%')
    ax.axis('equal')
    st.pyplot(fig)

# Define a function to display a correlation matrix
def display_correlation_matrix(df):
    corr_matrix = df.corr()
    # Create a mask to only show the lower triangle of the matrix
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', square=True, ax=ax)
    st.pyplot(fig)


st.title("Charts")
# Display a dropdown menu to select a variable for a histogram
st.header(":blue[Histogram]")
hist_variable = st.selectbox('**Select a variable for the histogram**', df.columns)
display_histogram(hist_variable)

# Display dropdown menus to select two variables for a scatterplot
st.header(":red[Scatter Plot]")
x_variable = st.selectbox('Select a variable for the x-axis of the scatterplot', df.columns)
y_variable = st.selectbox('Select a variable for the y-axis of the scatterplot', df.columns)
display_scatterplot(x_variable, y_variable)

# Display a dropdown menu to select a variable for a pie chart
st.header(":orange[Pie Chart]")
columns = ['species','island','sex']
pie_variable = st.selectbox('**Select a variable for the pie chart**', columns)
display_piechart(pie_variable)

# Display correlation matrix
st.header(":green[Correlation Matrix]")
display_correlation_matrix(df)