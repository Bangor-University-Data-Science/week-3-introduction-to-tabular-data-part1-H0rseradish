import pandas as pd

from titanic_analysis.data_loader import load_titanic_data
df = load_titanic_data('data/titanic.csv')

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    # Implement the logic here

    # Make a list of values for each column - is there a shorter way of doing this?
    feature_name_list = df.columns.tolist()
    print(feature_name_list)

    datatype_list = df.dtypes.tolist()
    print(datatype_list)

    number_unique_list = df.nunique().tolist()
    print(number_unique_list)

    # there MUST be an easier way to do this...
    # missing_values_df = df.loc[:, df.isna().any()]
    # print(missing_values_df)
    # resulting_list = missing_values_df.columns.tolist()
    # ok but now what - a loop?

    # ok -  this does it!:
    missing_values_list = df.isna().any().tolist()
    print(missing_values_list)
    
    # pass all the lists into a dict:
    dict = {'Feature Name': feature_name_list, 'Data Type': datatype_list, 'Number of Unique Values': number_unique_list, 'Has Missing Values?': missing_values_list }
    
    # create dataframe using the dict: 
    summary_df = pd.DataFrame(dict)
    print(summary_df)
    return summary_df

# print(create_summary_table(df))