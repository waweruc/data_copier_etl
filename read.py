from util import get_connection

def read_table(db_details, table_name, limit=0):
    source_db = db_details['source_db']
    connection = get_connection(db_type=source_db['db_type'],db_host=source_db['host'],db_name=source_db['database'],db_user=source_db['user'],db_pass=source_db['password'])
    cursor = connection.cursor()
    if limit == 0:
        query = f'select * from {table_name};'
    else:
        query = f'select * from {table_name} limit {limit};'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names

    connection.close()

    return data, column_names