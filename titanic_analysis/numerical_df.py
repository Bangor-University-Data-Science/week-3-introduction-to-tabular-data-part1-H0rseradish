import numpy as np
import pandas as pd

from titanic_analysis.data_loader import load_titanic_data

df = load_titanic_data('data/titanic.csv')
# checking the data is there:
# print(df.shape)

numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
# print to check expected data as a list:
# print(numerical_features)

def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    # Implement the logic here

    # First, I need to make a new dict to pass it to the dataframe to create it
    # numerical_data_dict = {}
    # ... I VASTLY OVERCOMPLICATED THIS AT FIRST..

    # my keys will be from numerical_features list
    
    # my values - need to get these from the df 
    numerical_cols_values = df.loc[:, numerical_features]# WHAAAAT it is JUST this ???!! - Yes!!!!
    # print(numerical_cols_values)
    return numerical_cols_values

print(get_numerical_df(df, numerical_features)) 