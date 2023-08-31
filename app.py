from util import load_db_details, get_tables
from read import read_table
from write import load_table

def main():
    # Retrieve the database details for the specified environment
    db_details = load_db_details('dev')
    tables = get_tables('table_list')

    for table_name in tables['table_name']:
        print(f'Reading data for table: {table_name}')
        data, column_names = read_table(db_details, table_name)
        print(f'Writing data for table: {table_name}')
        load_table(db_details, data, column_names, table_name)
if __name__ == '__main__':
    main()