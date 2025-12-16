import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yfin

from datetime import date

pd.options.display.float_format = "{:,.6f}".format


# 1.1 Taking a Look at the Data
# Starting and end dates
start = datetime.date(2019, 8, 1)
end = datetime.date(2024, 8, 1)

# Get data
# To switch between live data download and local data loading, 
# uncomment the desired line and comment out the other.
# Get Amazon, Ford and Bitcoin data
# df = yfin.download(["AMZN", "F", "BTC-USD"], start, end, auto_adjust = False)["Adj Close"]
df = pd.read_csv('financial data/Module2/lesson1/FD_M2_L1_stocks_data.csv', index_col='Date', parse_dates=True)\
                    .loc[start:end].reindex(columns=["AMZN", "F", "BTC-USD"])

# Convert DataFrame index to timezone-aware (UTC)
df.index = df.index.tz_localize('UTC')

# print(df.head(10))
# print(df.describe())



# Charting Prices over 2023

# # Create the figure.
# # We want a plot where the three assets have the same index (x-axis) but different scale (y-axis)
# fig = plt.figure(figsize=(13,7))
# ax1 = fig.add_subplot(111)
# ax2 = ax1.twinx()
# ax3 = ax1.twinx()

# # Plot the data
# df["2023-01-01":"2023-12-31"].plot(ax=ax1, y='AMZN', legend=True)
# df["2023-01-01":"2023-12-31"].plot(ax=ax2, y='BTC-USD', legend=True, color='g')
# df["2023-01-01":"2023-12-31"].plot(ax=ax3, y='F', legend=True, color='r')

# # We set the labels to the axes
# ax1.set_ylabel('AMZN')
# ax2.set_ylabel('BTC-USD')
# ax3.set_ylabel('F')
# ax3.spines['right'].set_position(('outward', 60))

# # Set position of legends
# ax1.legend(['AMZN'], loc='upper left')
# ax2.legend(['BTC-USD'], loc='upper left', bbox_to_anchor=(0, 0.95))
# ax3.legend(['F'], loc='upper left', bbox_to_anchor=(0, 0.9))

# plt.show()


## **2. Calculating Return on Investment

# Access the first row of the DataFrame
first_row = df.iloc[0]

# Assign price values to variables
amzn_price = first_row["AMZN"]
f_price = first_row["F"]
btc_price = first_row["BTC-USD"]

# Print price values
print("Purchase price of AMZN:", np.round(amzn_price, 3))
print("Purchase price of F:", np.round(f_price, 3))
print("Purchase price of BTC-USD:", np.round(btc_price, 3))
print(" - - - - - - - - - -")

# Divide $1,000 by each of price values to get number of shares
amzn_shares = 1000 / amzn_price
f_shares = 1000 / f_price
btc_shares = 1000 / btc_price

# Print number of shares for each ticker
print("Number of shares of AMZN:", np.round(amzn_shares, 3))
print("Number of shares of F:", np.round(f_shares, 3))
print("Number of shares of BTC-USD:", np.round(btc_shares, 3))


# Get last date values from df
last_row = df.iloc[-1]

# Assign end date price values to variables
amzn_price_end = last_row["AMZN"]
f_price_end = last_row["F"]
btc_price_end = last_row["BTC-USD"]

# print end date prices
print("End price of AMZN:", np.round(amzn_price_end, 3))
print("End price of F:", np.round(f_price_end, 3)) 
print("End price of BTC-USD:", np.round(btc_price_end, 3))

# Compute end date values for each ticker
amzn_value = amzn_price_end * amzn_shares
f_value = f_price_end * f_shares
btc_value = btc_price_end * btc_shares


# Print end date values
print("Holding value of AMZN:", np.round(amzn_value, 3))
print("Holding value of F:", np.round(f_value, 3))
print("Holding value of BTC-USD:", np.round(btc_value, 3))



