import mysql.connector


def get_connection():

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Parveen@78638",
            database="ONLINE_EXAMINATION_SYSTEM3"
        )

        if connection.is_connected():
            print("MySQL connection successful!")
            print("Database: ONLINE_EXAMINATION_SYSTEM3")

        return connection

    except mysql.connector.Error as error:
        print("MySQL connection failed!")
        print("Error:", error)
        return None