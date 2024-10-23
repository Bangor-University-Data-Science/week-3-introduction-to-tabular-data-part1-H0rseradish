from titanic_analysis.data_loader import load_titanic_data

df = load_titanic_data('data/titanic.csv')
categorical_features = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
# and this prints a list of the categorical column names:
# print(categorical_features)

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.

    """
    # Implement the logic here

    # need to return a dict:
    categorical_unique_values = {}

    # this prints all the categorical columns and their values as a dataframe:
    # categorical_columns = df[categorical_features]
    # print(categorical_columns) # BUT I need to filter values using unique...

    # using unique on each col in categorical features columns - the condition has to go before the loop:
    categorical_unique_lists = [df[col].unique().tolist() for col in df[categorical_features]]
    # prints an array of lists: 
    # print(categorical_unique_lists)
    
    # now make a dict with these: woohoo zip works for lists of the same length!:
    categorical_unique_values = dict(zip(categorical_features, categorical_unique_lists))

    # return the dict:
    return categorical_unique_values
    

# print(display_unique_values(df, categorical_features))