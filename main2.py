import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard de Vacinação dos países")

df = pd.read_csv("vacinacao_corrigido.csv")

df['date'] = pd.to_datetime(df['date'])

fig1 = px.line(df, 
               x = 'date', 
               y = 'total_vaccinations', 
               color = 'location', 
               title = 'Total de Vacinações por Data e País')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Total de Vacinações', title_font_size = 30)
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

df_filtro = df.query('location == "BRAZIL" or location == "INDIA" or location == "UNITED STATES"')

fig2 = px.pie(df_filtro, values='people_fully_vaccinated', names='location', 
              title='Pessoas Totalmente Vacinadas do Brasil, India e USA')
fig2.update_layout(title_font_size = 30)
fig2.show()

st.plotly_chart(fig2, use_container_width=True)
