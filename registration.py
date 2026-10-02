from database import get_connection


def register_student():

    print("\n==============================")
    print("      STUDENT REGISTRATION")
    print("==============================")

    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students
        (full_name, email, password)
        VALUES (%s, %s, %s)
    """

    try:

        cursor.execute(
            query,
            (full_name, email, password)
        )

        connection.commit()

        print("\nRegistration successful!")

    except Exception as e:

        connection.rollback()

        print("\nRegistration failed.")
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()
