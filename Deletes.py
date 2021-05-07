import mysql.connector
from mysql.connector import Error


def delete(query):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        sql_select_query = query
        cursor.execute(sql_select_query)
        connection.commit()
        print("Record Deleted successfully ")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
