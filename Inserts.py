import mysql.connector


def insertArt(Name, Description, Category, Artist, Gallery, Price):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        insert_query = """INSERT INTO Art (Name, Description, Category, Artist, Gallery, Price) 
                                VALUES (%s, %s, %s, %s, %s, %s) """

        record = (Name, Description, Category, Artist, Gallery, Price)
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insertArtist(Name, Lastname, National_ID, Phone_Number, Age):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        insert_query = """INSERT INTO Artist (Name, Lastname, National_ID, Phone_Number, Age) 
                                VALUES (%s, %s, %s, %s, %s) """

        record = (Name, Lastname, National_ID, Phone_Number, Age)
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insertAuction(Date, Gallery):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        insert_query = """INSERT INTO Auction (Date, Gallery)
                        VALUES (%s, %s) """
        record = (Date, Gallery)
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print(cursor.statement)
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insertGallery(Name, Opening_Date, Closing_Date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        insert_query = """INSERT INTO Gallery (Name, Opening_Date, Closing_Date)
                        VALUES (%s, %s, %s) """
        record = (Name, Opening_Date, Closing_Date)
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print(cursor.statement)
        print("Failed to insert into MySQL table {}".format(error))
        #raise

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insertCustomer(Name, Lastname, Phone_Number):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        insert_query = """INSERT INTO Customer (Name, Lastname, Phone_Number)
                        VALUES (%s, %s, %s) """
        record = (Name, Lastname, Phone_Number)
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insertReciept(Customer, Artist, Auction, Suggested_Price):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Picto_Gallery',
                                             user='root',
                                             password='pwdpwd')
        cursor = connection.cursor()
        insert_query = """INSERT INTO Reciept (Customer, Artist, Auction, Suggested_Price)
                        VALUES (%s, %s, %s) """
        record = (Customer, Artist, Auction, Suggested_Price)
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


