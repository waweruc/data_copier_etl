# data_copier_etl
ETL Pipeline for Dynamic Data Copying This ETL pipeline copies data dynamically from a source database to a target database. The pipeline is implemented in Python and uses the following technologies:

Pandas: A Python library for data manipulation and analysis psycopg2 and mysql.connector: A Python library for interacting with databases

The pipeline works as follows: The pipeline first reads the configuration file, which specifies the source database, target database, and table names. The pipeline then queries the source database for the data to be copied. The pipeline consults the table_list file to determine which tables are to be loaded to the target. The pipeline then loads the data into the target database. The pipeline is designed to be dynamic, so it can be easily modified to copy data from different sources and destinations. The pipeline is also scalable, so it can be used to copy large amounts of data.
