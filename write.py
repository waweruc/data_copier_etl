from util import get_connection

def build_insert_query(table_name, column_names):
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column,'%s'),column_names))
    column_values_string = ', '.join(column_values)
    query = f'''
    INSERT INTO {table_name} ({column_names_string}) VALUES ({column_values_string});
    '''
    return query

def insert_data(connection, cursor, query, data, batch_size=100):
    records = []
    count = 1
    for record in data:
        records.append(record)
        if count % batch_size == 0:
            cursor.executemany(query, records)
            connection.commit()
            records = []
        count=+1
    cursor.executemany(query, records)
    connection.commit()

def load_table(db_details, data, column_names, table_name):
    target_db = db_details['target_db']
    connection = get_connection(db_type=target_db['db_type'],db_host=target_db['host'],db_name=target_db['database'],db_user=target_db['user'],db_pass=target_db['password'])
    cursor = connection.cursor()
    query = build_insert_query(table_name, column_names)
    insert_data(connection, cursor, query, data)

    connection.close()
