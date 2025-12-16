# Load the dataset for analysis

import pandas as pd
import numpy as np

# Define the yeild CSV filename
TEST_CSV_FILE = 'financial data/Module1/CodeTask/US_Yields.csv'

# Load the csv dataset
df = pd.read_csv(TEST_CSV_FILE, index_col = 0)
df.index = pd.to_datetime(df.index)

df.head()






# ##############################################
# # FD-GCA-M1-Q1
# ###############################################
# # Create a function to investigate the dataset

# def investigate_data(df):
#     """
#     Investigate the loaded yield data and return summary statistics.
    
#     Parameters:
#     -----------
#     df : pandas.DataFrame
#         The loaded yield data
    
#     Returns:
#     --------
#     dict
#         Dictionary containing data investigation results
#     """
#     ####################################
#     # # TODO: Complete your code here
#     # ####################################
#     # # Hint: Use df.shape to find row number and column number of the dataset
#     num_rows, num_columns = df.shape
#     # # Hint: Use df.index, min() and strftime to find the earliest date of the datas
#     earliest_date = df.index.min().strftime('%Y-%m-%d')
    
#     # # Hint: Use df.index, max() and strftime to find the latest date of the dataset
#     latest_date = df.index.max().strftime('%Y-%m-%d')
#     # # Hint: Use tolist() to find column names of the dataset
#     column_names = df.columns.tolist()

    
#     # print(num_columns)

#     return {
#         'num_rows': num_rows,
#         'num_columns': num_columns,
#         # 'date_range': (earliest_date, latest_date),
#         # 'column_names': column_names
#     }





##############################################
# FD-GCA-M1-Q3
###############################################
# Create a function to investigate the dataset

date = df.index.strftime('%Y-%m-%d')


def analyze_yield_curve_from_data(df, date):
    """
    Analyze the yield curve for a specific date using 2-year and 10-year yields.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The loaded yield data with datetime index
    date : str
        Date in 'YYYY-MM-DD' format
    
    Returns:
    --------
    tuple : (float, float, tuple)
        A tuple containing:
        - yield_2y: The 2-year yield value
        - yield_10y: The 10-year yield value
        - analysis: A tuple (slope, shape) where slope is float and shape is string
    """
    ####################################
    # TODO: Complete your code here
    ####################################

    # Hint: Convert date string to datetime: pd.to_datetime(date)
    date_dt = pd.to_datetime(date)
    # Check if date exists in the DataFrame
    if not df.index.isin([date_dt]).any():
        raise ValueError(f"Date {date} not found in the dataset.")
    # Hint: Extract 2-year and 10-year yields using df.loc[]
    # Assuming columns are named '2Y' and '10Y' (adjust if different)
    yield_2y = df.loc[date_dt]
    yield_10y = df.loc[date_dt]
    # Hint: Calculate slope = yield_10y - yield_2y
    slope = yield_10y - yield_2y
    # Hint: Classify shape based on slope (slope >0.1: "normal", abs(slope) <=0.1: "flat", else: "inverted")
    if slope > 0.1:
        shape = "normal"
    elif abs(slope) <= 0.1:
        shape = "flat"
    else:
        shape = "inverted"
    # Return the complete analysis
    return (float(yield_2y), float(yield_10y), (float(slope), shape))








##############################################
# FD-GCA-M1-Q5
###############################################
# Construct Nelson Siegel Formula

def nelson_siegel(maturity, beta_0, beta_1, beta_2, lambda_param):
    """
    Calculate yields using the Nelson-Siegel model.
    
    Parameters:
    -----------
    maturity : numpy array
        Time to maturity in years
    beta_0 : float
        Level parameter
    beta_1 : float
        Slope parameter
    beta_2 : float
        Curvature parameter
    lambda_param : float
        Decay rate parameter (positive)
    
    Returns:
    --------
    numpy array
        Predicted yield(s)
    """
    ####################################
    # Completed code using hints
    ####################################   
    # Hint: Calculate lambda * maturity
    lambda_t = lambda_param * np.asarray(maturity)
    
    # Hint: Calculate exponential term using np.exp()
    exp_term = np.exp(-lambda_t)
    
    # Hint: Calculate factor1: (1 - exp(-lambda*t)) / (lambda*t)
    # Avoid division by zero for lambda_t = 0
    factor1 = np.where(lambda_t == 0, 1.0, (1 - exp_term) / lambda_t)
    
    # Hint: Calculate factor2: factor1 - exp(-lambda*t)
    factor2 = factor1 - exp_term
    
    # Hint: Calculate yield using Nelson-Siegel formula
    yield_value = beta_0 + beta_1 * factor1 + beta_2 * factor2
    
    return yield_value









# investigate_data(df)