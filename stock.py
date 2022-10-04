import streamlit as st
import pandas as pd
import yfinance as yf
# import datetime as dt
st.set_page_config(layout='wide')

with st.sidebar:
    st.title('Stock Price')
    tickerSymbol = st.radio('Pick Stock', ["GOOGL", "AAPL", "TSLA"])
    # tickerSymbol = st.text_input("Enter Ticker Symbol")
    selectPeriod = st.select_slider("Select Period", ["1d", "5d", "1mo"])
    # , start='2022-01-01', end=dt.datetime.now()

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period=selectPeriod)

c1, c2 = st.columns(2)

with c1:
    st.header("Chart (%s) - %s" % (tickerSymbol, selectPeriod))
    st.line_chart(tickerDf['Close'])

with c2:
    st.header("Dataframe (%s) - %s" % (tickerSymbol, selectPeriod))
    st.dataframe(tickerDf)
