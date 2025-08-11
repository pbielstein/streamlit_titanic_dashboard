import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Titanic Dashboard')

df = pd.read_csv('titanic.csv')

df['Embarked'] = df['Embarked'].fillna('Unkown')

# get unique values for Embarked
embarked_port = df['Embarked'].unique().tolist()
gender = df['Sex'].unique().tolist()

col1, col2 = st.columns([1, 1])
selected_port = col1.selectbox(options=embarked_port, label='Select a port')
selected_gender = col2.selectbox(options=gender, label='Select a gender')