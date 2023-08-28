from config import connection_details
from util import get_tables

def main():
    env = "dev"

    # Retrieve the database details for the specified environment
    db_details = connection_details[env]

    # Get the tables that will be loaded from util.py
    tables = get_tables('table_list')
    for table in tables['table_name']:
        print(table)

if __name__ == '__main__':
    main()