

import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',       
        password='Averystrongpassword',   
        database='products_db'
    )
    return connection
