import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()




# Initialize the FRED API with your key
fred = Fred(api_key='e72ea47c1be7b999042c53a23868545b ') # "YOUR_API_KEY"

# List of Treasury yield series IDs
series_ids = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS5', \
              'DGS7', 'DGS10', 'DGS20', 'DGS30']

# Function to get data for a single series
def get_yield_data(series_id):
    data = fred.get_series(series_id, observation_start="1975-01-01", observation_end="2024-05-03")
    return data

# Get data for all series
yields_dict = {series_id: get_yield_data(series_id) for series_id in series_ids}

# Combine into a single DataFrame
yields = pd.DataFrame(yields_dict)

# Rename columns for clarity
yields.columns = ['1 Month', '3 Month', '6 Month', '1 Year', '2 Year', '3 Year', '5 Year', \
                  '7 Year', '10 Year', '20 Year', '30 Year']






# yields.index = pd.to_datetime(yields.index)
# yields.loc['2020-01-03']



# yields.isna().sum(axis = 0)



# We can see that during the days that the 10-year is not reported,
# none maturity is reported as well.

# yields[yields['10 Year'].isna() == True].sum(axis = 0)




# Figure 1
yields.plot(figsize=(12, 8), title='Treasury Yields', alpha=0.7) # Plot the yields
plt.show()



# Figure 2
# sns.pairplot(yields.dropna(), diag_kind='kde') # Pairplot with KDE on the diagonal
# plt.suptitle("Pairwise Distribution and KDE of Daily Yield Data (2001-07-31 to 2024-05-03)",
#              y=1.02, fontsize=26)
# plt.show()



# Figure 3

# def plot_yield_curve(date):
#     maturities = ['1M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'] # Maturities
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(maturities, yields.loc[date], marker='D', label='Yield Curve at ' + date)

#     ax.set_yticklabels(['{:.2f}%'.format(y) for y in ax.get_yticks()])
#     ax.set_xticks(range(len(maturities)))
#     ax.set_xticklabels(maturities)

#     # Add labels and title
#     ax.set_xlabel('Maturity')
#     ax.set_ylabel('Yield')
#     ax.set_title('Treasury Yield Curve')

#     fig.legend(loc = [0.69, 0.14])

#     # Show the plot
#     plt.grid(True)
#     plt.show()

# plot_yield_curve('2020-01-03')