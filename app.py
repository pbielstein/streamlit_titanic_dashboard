import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.title('Titanic Dashboard')

df = pd.read_csv('titanic_data.csv')

df['Embarked'] = df['Embarked'].fillna('Unkown')

# get unique values for Embarked
embarked_port = df['Embarked'].unique().tolist()
gender = df['Sex'].unique().tolist()

col1, col2 = st.columns([1, 1])
selected_port = col1.selectbox(options=embarked_port, label='Select a port')
selected_gender = col2.selectbox(options=gender, label='Select a gender')

# filter dataframe based on selections
df_plot = df[(df['Embarked'] == selected_port) & (df['Sex'] == selected_gender)]

plot = px.histogram(data_frame=df_plot,
                    template='seaborn',
                    color='Survived',
                    title=f'Distribution of age',
                    facet_col='Survived',
                    x='Age'
)
st.plotly_chart(plot)