import mysql.connector
from mysql.connector import Error


def selecting(query):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor(buffered=True)
        sql_select_query = query
        cursor.execute(sql_select_query)
        print("Total number of rows: ", cursor.rowcount)
        connection.commit()
        print("Record Selected successfully ")

        result = cursor.fetchall()

        a = []
        for x in result:
            a.append(x)
        return a

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

