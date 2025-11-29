import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard de Covid-19")

df = pd.read_csv('WHO_time_series.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df, 
               x = 'Date_reported', 
               y = 'Cumulative_cases', 
               color = 'Country', 
               title = 'Dados de COVID-19 no mundo - Ano 2020')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados', title_font_size = 30)
fig1.show()

st.plotly_chart(fig1, use_container_width = True)


df_brasil_usa_india = df.query('Country in ["Brazil", "India", "United States of America"]')

fig2 = px.pie(df_brasil_usa_india, values='Cumulative_cases', names='Country', 
              title='Comparativo entre os Casos Acumulados de Basil, USA e India')
fig2.update_layout(title_font_size = 30)
fig2.show()

st.plotly_chart(fig2, use_container_width = True)
