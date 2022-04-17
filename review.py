import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# InaccUrate Rating Prediction App
This app predicts the **Inaccurate** Ratings!
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        ID = st.sidebar.selectbox('ID', list((range(3886,684991))))
        Star = st.sidebar.selectbox('Star',list(range(1,5)))
        data = {'ID':ID,
               'Star':Star
                }             
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
st.write(input_df)
st.subheader('Prediction')
cleaned_data= pd.read_csv('Cleaned_reviews.csv')
st.write(cleaned_data)
