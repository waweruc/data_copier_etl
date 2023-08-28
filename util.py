import pandas as pd

# Define a function that will get tables that will have their data loaded from the table_list file
def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded=="yes"')
