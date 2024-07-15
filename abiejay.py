import pandas as pd
import altair as alt
import streamlit as st
st.header('week1 report')
st.sidebar.subheader('Team performance')
df=pd.read_csv('revenue file.csv')
total = df['TOTAL'].str.replace(',', '').astype(float)
scatter=alt.Chart(df).mark_circle().encode(
    x='TEAMS', 
    y='TOTAL',
    color='TEAMS',
    tooltip=['27/5/2024', '28/5/2024', '29/5/2024', '30/5/2024', '31/5/2024']
).properties(
    title='THIS IS A SCATTERPLOT',
    width=600,
    height=400
).interactive()
st.dataframe(df)
st.altair_chart(scatter)