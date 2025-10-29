
# Real Time Stock Price Dashboard

A real-time interactive stock price dashboard built with Streamlit and yfinance — displays live stock data, key metrics and a matplotlib line chart for any ticker symbol.

## 🚀 Features
- Enter any stock ticker symbol (e.g., AAPL, MSFT, AMZN)
- Choose period (1d, 5d, 1mo, 3mo, 6mo, 1y, 5y) and interval (1m, 5m, 15m, 1h, 1d)
- Automatically fetches latest stock close-price data using yfinance
- Displays current price, change and percentage change in the sidebar
- Displays a line chart (matplotlib) of closing prices for the selected period
- Shows recent data table (last 10 rows)
- Clean UI with easy sidebar controls

## 🛠️ Built With
- [Streamlit](https://streamlit.io)  
- [yfinance](https://github.com/ranaroussi/yfinance)  
- [pandas](https://pandas.pydata.org)  
- [matplotlib](https://matplotlib.org)  
- Python 3.x

## 📋 Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Mananwadhwa52/Real_Time_Stock_Price_Dashboard.git
   cd Real_Time_Stock_Price_Dashboard
````

2. (Optional) Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install streamlit yfinance pandas matplotlib
   ```
4. Run the app:

   ```bash
   streamlit run stock_dashboard.py
   ```
5. The app will open in your default web browser. Use the sidebar to input a ticker, select period/interval, toggle auto-adjust, etc.

## 🔍 Usage Example

* Enter ticker: `AAPL`
* Period: `1mo`
* Interval: `1d`
* Auto-adjust: ✔ or ✘
  The dashboard will display the latest Apple Inc. stock price, change in USD and %, plot the closing price chart and show recent rows of data.

## 🧩 Customisation

* Add other technical indicators (SMA, EMA, RSI) by extending the code.
* Support “candlestick” charts by replacing matplotlib with mplfinance or other libraries.
* Add multi-ticker support (compare two or more tickers).
* Integrate caching (e.g., Streamlit caching) to reduce repeated API calls.

## 🐛 Known Issues

* Some tickers may fail if yfinance cannot fetch data (due to delisting or API issues).
* Very short periods may return insufficient data for computing change/percentage change.
* Interval choices like `1m`, `5m` may only be supported for recent periods (depending on yfinance limitations).

## 💡 License

This project is open-source and distributed under the MIT License. See the `LICENSE` file for details.

## 👤 Author

Your Name – Manan wadhwa
GitHub: [@Mananwadhwa52](https://github.com/Mananwadhwa52)
