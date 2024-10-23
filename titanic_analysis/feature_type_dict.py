import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

df = load_titanic_data('data/titanic.csv')

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    # get numerical continuous column names as list
    numerical_continuous = df.select_dtypes(include=['float64']).columns.tolist()
    # update the dict's nested keys list:
    feature_types['numerical']['continuous'] = numerical_continuous

    # get numerical discrete column names
    numerical_discrete = df.select_dtypes(include=['int64']).columns.tolist()
    # boolean = df.nunique() == 2
    # print(boolean)
    feature_types['numerical']['discrete'] = numerical_discrete

    #get categorical nominal
    categorical_nominal = df.select_dtypes(include=['object', 'boolean']).columns.to_list()
    # update the dict
    feature_types['categorical']['nominal'] = categorical_nominal

    # theoretically get categorical ordinal - won't work for titanic set because the 'category' dtype is not in the dataset!
    categorical_ordinal = df.select_dtypes(include=['category', ]).columns.to_list()
    # update the dict
    feature_types['categorical']['ordinal'] = categorical_ordinal


    return feature_types

print(create_feature_type_dict(df))
