import streamlit as st
import pandas as pd

df = pd.read_csv('store.csv')

st.set_page_config(layout='wide')

st.title("Ini dashboard latihan")
st.write("Nama saya siroj")
st.code('pip install watchdog')

st.metric(label="Sales", value="1.35M USD", delta="7.4%")

st.dataframe(df)
st.header('Chart Sales')
st.line_chart(df['Sales'])
st.header('Chart Profit')
st.area_chart(df['Profit'])
st.header('Chart Quantity')
st.bar_chart(df['Quantity'])
