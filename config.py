import os
# Database connection details
connection_details = { 
    'dev' : { 
            'source_db' : {
                'db_type' : 'mysql',
                'host' : 'localhost',
                'database' : 'retail_db',
                'user': os.environ.get('RETAIL_DB_USER'),
                'password': os.environ.get('RETAIL_DB_PASS')
                },
            'target_db' : { 
                'db_type' : 'postgres',
                'host' : 'localhost',
                'database' : 'retail_db',
                'user': os.environ.get('CUSTOMER_DB_USER'),
                'password': os.environ.get('CUSTOMER_DB_PASS')
                }
             } 
            }
