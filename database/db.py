import mysql.connector
from mysql.connector import connect, Error
from database.config import Config

def get_db_connection():
    try:
        connection = connect(
            host=Config.MYSQL_HOST,
            database=Config.MYSQL_DB,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD
        )
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None
    
def execute_query(query, params=None):
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error: '{e}'")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetch_query(query, params=None):
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: '{e}'")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def test():
    return "test"
