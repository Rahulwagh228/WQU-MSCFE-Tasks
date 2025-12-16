##############################################
    # FD-GCA-M1-Q3
    ###############################################
    # Create a function to investigate the dataset


    import pandas as pd
    import numpy as np

    # Define the yeild CSV filename
    TEST_CSV_FILE = 'financial data/Module1/CodeTask/US_Yields.csv'

    # Load the csv dataset
    df = pd.read_csv(TEST_CSV_FILE, index_col = 0)
    df.index = pd.to_datetime(df.index)

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

        # Ensure required columns exist in the DataFrame
        required_columns = ['2Y', '10Y']
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"Required column '{col}' is missing from the dataset.")

        # Extract 2-year and 10-year yields using df.loc()
        try:
            yield_2y = df.loc[date_dt, '2Y']
            yield_10y = df.loc[date_dt, '10Y']
        except KeyError as e:
            raise KeyError(f"Missing required columns in the dataset: {e}")

        # Calculate slope = yield_10y - yield_2y
        slope = yield_10y - yield_2y

        # Classify shape based on slope
        if slope > 0.1:
            shape = "normal"
        elif abs(slope) <= 0.1:
            shape = "flat"
        else:
            shape = "inverted"

        # Return the complete analysis
        return (float(yield_2y), float(yield_10y), (float(slope), shape))