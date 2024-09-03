import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date

# Get the latest 1-year stock data for AAPL
stock_data = yf.Ticker("AAPL").history(period="1y")

# Plot the closing price over time
plt.figure(figsize=(12,6))
plt.plot(stock_data.index, stock_data['Close'], label='Closing Price')

# Set title and labels
plt.title(f'AAPL Stock Price (Jun {date.today().year})')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()

# Save the plot as a PNG image
plt.savefig('aapl_stock_price.png', bbox_inches='tight')

print("Plot saved to aapl_stock_price.png")