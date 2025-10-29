# stock_dashboard.py

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_data(ticker: str, period: str = "1mo", interval: str = "1d", auto_adjust: bool=False) -> pd.DataFrame:
    try:
        df = yf.download(
            ticker,
            period=period,
            interval=interval,
            auto_adjust=auto_adjust,
            progress=False,
            threads=False
        )
        if df.empty:
            st.error(f"No data found for ticker {ticker}")
        return df
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()

def format_price_metrics(df: pd.DataFrame):
    if len(df) < 2:
        return None, None, None
    last_price = float(df['Close'].iloc[-1])
    prev_price = float(df['Close'].iloc[-2])
    change = last_price - prev_price
    pct_change = (change / prev_price) * 100 if prev_price != 0 else 0
    return last_price, change, pct_change

def plot_price_chart_matplotlib(df: pd.DataFrame, title: str = ""):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], label='Close Price', color='blue', linewidth=2)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)  # shows the matplotlib figure in Streamlit
    plt.close()     # close the figure after showing to avoid overlap

def main():
    st.set_page_config(page_title="Stock Dashboard", layout="wide")
    st.sidebar.title("Stock Dashboard Controls")

    ticker = st.sidebar.text_input("Stock Ticker Symbol", value="AAPL").upper().strip()
    period = st.sidebar.selectbox("Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y"], index=2)
    interval = st.sidebar.selectbox("Interval", ["1m", "5m", "15m", "1h", "1d"], index=4)
    chart_type = st.sidebar.radio("Chart Type", ["line"])  # only 'line' since we're using matplotlib line plot
    auto_adjust = st.sidebar.checkbox("Auto-adjust (splits/dividends)", value=False)

    st.title(f"Stock Dashboard for {ticker}")

    df = fetch_data(ticker, period=period, interval=interval, auto_adjust=auto_adjust)
    if df.empty:
        st.stop()

    last_price, change, pct_change = format_price_metrics(df)

    if last_price is None:
        st.warning("Not enough data to compute metrics.")
    else:
        st.sidebar.metric(label=f"{ticker} Price", value=f"${last_price:.2f}", delta=f"{change:.2f} ({pct_change:.2f}%)")

    st.write("### Price Chart")
    plot_price_chart_matplotlib(df, title=f"{ticker} Closing Price")

    st.write("### Recent Data")
    st.dataframe(df.tail(10))

if __name__ == "__main__":
    main()
