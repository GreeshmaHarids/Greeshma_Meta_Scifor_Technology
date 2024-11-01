import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from stocknews import StockNews
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


# Helper function to calculate moving averages
def calculate_moving_averages(data):
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()
    return data


def get_realtime_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        try:
            # Fetch the latest market data
            latest_data = stock.history(period="1d").iloc[-1]
            data[ticker] = {
                "Close": latest_data['Close'],
                "Open": latest_data['Open'],
                "Change (%)": ((latest_data['Close'] - latest_data['Open']) / latest_data['Open']) * 100,
                "Market Cap": stock.info['marketCap'],
                "PE Ratio": stock.info.get('trailingPE', 'N/A'),
                "Dividend Yield": stock.info.get('dividendYield', 'N/A')
            }
        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {e}")

    return pd.DataFrame(data).T


st.set_page_config(layout="wide")
st.title(":violet[Stock Market Dashboard]")

# Sidebar for page selection
page = st.sidebar.selectbox("Select Page", ["Home", "Comparative Analysis"])





# Sidebar inputs for stock symbol, date range, and timeframe
ticker = st.sidebar.text_input("Ticker Symbol")
start_date = st.sidebar.date_input("Start Date", key="start")
end_date = st.sidebar.date_input("End Date", key="end")
timeframe = st.sidebar.selectbox("Select Timeframe", ["Daily", "Weekly", "Monthly"])

@st.cache_data
def fetch_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data


# Check if the page is User Guidelines

# Fetch stock data if ticker is provided
if ticker:
    if st.button("Fetch Data"):
        with st.spinner("Fetching data..."):
            try:
                market_data = fetch_data(ticker)
                st.success("Data fetched successfully!")
                # Display data
                st.write(market_data)

                # CSV download button
                csv = market_data.to_csv().encode('utf-8')
                st.download_button("Download CSV", csv, "market_data.csv", "text/csv")
            except Exception as e:
                st.error(f"Error fetching market data: {e}")

    try:
        ticker_data = yf.Ticker(ticker)
        real_time_price = ticker_data.info['currentPrice']
        st.write(f"**Current Price of {ticker}:** ${real_time_price}")
        data = yf.download(tickers=ticker, start=start_date, end=end_date)

        # Handle case where data is empty
        if data.empty:
            st.error("No data found for the given ticker and date range. Please try another ticker.")
        else:
            # Fill null values
            data.fillna(method='ffill', inplace=True)

            # Resample data based on the selected timeframe
            if timeframe == "Weekly":
                data = data.resample('W').mean()  # Resample to weekly data
            elif timeframe == "Monthly":
                data = data.resample('M').mean()  # Resample to monthly data
            
        

            if page == "Home":
                # Home page content
                st.subheader("Stock Price Trends")
                # Convert 'Adj Close' to 1D 
                adj_close = data['Adj Close'].squeeze()
                fig = px.line(data, x=data.index, y=adj_close, title=ticker)
                st.plotly_chart(fig)

                # Calculate moving averages
                data_m = calculate_moving_averages(data)
                close_d = data_m['Close'].squeeze()
                ma_50 = data_m['50_MA'].squeeze()
                ma_200 = data_m['200_MA'].squeeze()

                # Create a figure using Plotly Graph Objects
                fig = go.Figure()

                # Add the Close price scatter trace
                fig.add_trace(go.Scatter(
                    x=data_m.index,
                    y=close_d,
                    mode='lines',
                    name='Close Price',
                    line=dict(color='blue', width=2)
                ))

                # Add the 50-day moving average trace
                fig.add_trace(go.Scatter(
                    x=data_m.index,
                    y=ma_50,
                    mode='lines',
                    name='50-day MA',
                    line=dict(color='orange', width=1),
                    fill='tozeroy'
                ))

                # Add the 200-day moving average trace
                fig.add_trace(go.Scatter(
                    x=data_m.index,
                    y=ma_200,
                    mode='lines',
                    name='200-day MA',
                    line=dict(color='green', width=2)
                ))

                # Update layout for better visuals
                fig.update_layout(
                    title=f"{ticker} Stock Price with 50-day and 200-day Moving Averages",
                    xaxis_title='Date',
                    yaxis_title='Price',
                    legend_title='Legend'
                )

                # Show the chart in Streamlit
                st.plotly_chart(fig)

                # Display financial statements
                pricing_data, news = st.tabs(["Pricing Data", "Top 10 News"])
                with pricing_data:
                    st.header("Pricing Movements")
                    data2 = data.copy()
                    data2["% Change"] = data2['Adj Close'] / data2['Adj Close'].shift(1) - 1
                    data2.dropna(inplace=True)
                    st.write(data2)
                    annual_return = data2["% Change"].mean() * 252 * 100
                    st.write("Annual Return is ", annual_return, "%")
                    stdev = np.std(data2["% Change"]) * np.sqrt(252)
                    st.write('Standard Deviation is ', stdev * 100, "%")
                    st.write('Risk Adj. Return is ', annual_return / (stdev * 100))

                with news:
                    st.header(f"News of {ticker}")
                    sn = StockNews(ticker, save_news=False)
                    df_news = sn.read_rss()
                    for i in range(10):
                        st.write(df_news['published'][i])
                        if df_news["sentiment_title"][i] >= 0:
                            color = '#006400'
                        else:
                            color = '#8B0000'

                        html_string = f'<h3><span style="color: {color};">{df_news["title"][i]}</span></h3>'
                        st.markdown(html_string, unsafe_allow_html=True)
                        st.write(df_news['summary'][i])
                        st.write(f"Title Sentiment: {df_news['sentiment_title'][i]}")
                        st.write(f"News Sentiment: {df_news['sentiment_summary'][i]}")
                        st.divider()

            elif page == "Comparative Analysis":
                # Comparative Analysis page content
                compare_tickers = st.sidebar.text_input("Enter another ticker to compare")

                if compare_tickers:
                    try:
                        ticker_data_c = yf.Ticker(compare_tickers)
                        real_time_price_c = ticker_data_c.info['currentPrice']
                        st.write(f"**Current Price of {compare_tickers}:** ${real_time_price_c}")
                        st.subheader("Comparative Analysis")

                        # Moving Average Filter (choose moving averages to display)
                        show_50_ma = st.checkbox("50-Day Moving Average", value=False)
                        show_200_ma = st.checkbox("200-Day Moving Average", value=False)

                        compare_symbols = [ticker, compare_tickers]
                        comparison_data = pd.DataFrame()

                        for symbol in compare_symbols:
                            compare_data = yf.download(symbol, start=start_date, end=end_date)
                            compare_data = calculate_moving_averages(compare_data)  # Ensures required MAs are calculated
                            comparison_data[symbol] = compare_data['Adj Close']

                        # Plot comparative data
                        fig = go.Figure()

                        # Plot each stock’s adjusted close and selected moving averages
                        for symbol in compare_symbols:
                            fig.add_trace(go.Scatter(x=comparison_data.index, y=comparison_data[symbol], mode='lines', name=symbol))

                            # Plot moving averages based on user selection
                            if show_50_ma:
                                fig.add_trace(go.Scatter(x=compare_data.index, y=compare_data['50_MA'], mode='lines',
                                                          name=f"{symbol} 50-Day MA", line=dict(dash='dash')))
                            if show_200_ma:
                                fig.add_trace(go.Scatter(x=compare_data.index, y=compare_data['200_MA'], mode='lines',
                                                          name=f"{symbol} 200-Day MA", line=dict(dash='dot')))

                        # Layout updates
                        fig.update_layout(title="Comparative Stock Prices with Moving Averages",
                                          xaxis_title="Date",
                                          yaxis_title="Price (Adj Close)")
                        st.plotly_chart(fig)
                    except Exception as e:
                        st.error(f"Error fetching comparative data: {e}")
                
            
                
    except Exception as e:
        st.error(f'Error enter valid data')

else:
    st.warning("Please enter a ticker symbol.")
