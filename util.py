import pandas as pd
from config import connection_details
import mysql.connector as mc
import psycopg2
from mysql.connector import Error as ec

# Function to get db details
def load_db_details(env):
    return connection_details[env]

# Get mysql connection details
def get_mysql_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mc.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
    except mc.Error as error:
        if error.errno == ec.Errr_Access_Denied:
            print("Invalid Credentials")
        else:
            print(error)
    return connection

# Get pg connection details
def get_pg_connection(db_host, db_name, db_user, db_pass):
    connection = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)

def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
       connection = mc.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
    if db_type == 'postgres':
        connection = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
    return connection

# Function that will get tables that will have their data loaded from the table_list file
def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded=="yes"')
