import psycopg2
from psycopg2 import Error

def connect_db(username = 'raywu1990', pwd = 'test',
               host = '127.0.0.1', port = '5432', db = 'dvdrental'):

        try:
            connection = psycopg2.connect(user = username,
                                          password = pwd,
                                          host = host,
                                          port = port,
                                          database = db)
            cursor = connection.cursor()
            print("Connected to the database.")
            return cursor, connection
        except(Exception, Error) as error:
            print("Error connection to the database.", error)
            return -1

def disconnect_db(connection, cursor):

    if connection:
        cursor.close()
        connection.close()
        print("Disconnected from the database.")
    else:
        print("Error with the connection.")


def run_sql(cursor, sql_str):

    try:
        cursor.execute(sql_str)
        record = cursor.fetchall()
        return record
    except(Exception, Error) as error:
        print("Error executing the code.", error)
        return -1
