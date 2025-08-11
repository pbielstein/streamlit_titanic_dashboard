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
col1.plotly_chart(plot)

# create pie chart using plotly express
df_plot_pie = df_plot.loc[:, ['PassengerId', 'Survived']].groupby(['Survived']).count().reset_index()
df_plot_pie.rename(columns={'PassengerId': 'Count of passengers'}, inplace=True)
pie_plot = px.pie(df_plot_pie,
                  template='seaborn',
                  title=f'Count of passengers that survived',
                  values='Count of passengers',
                  names='Survived',)

col2.plotly_chart(pie_plot)

# add a boxplot of the fare prices
box_plot = px.box(df_plot,
                  y='Fare',
                  x='Survived',
                  template='seaborn',
                  title=f'Fare prices by survival status',
                  color='Survived')
# attach to dashboard
st.plotly_chart(box_plot)