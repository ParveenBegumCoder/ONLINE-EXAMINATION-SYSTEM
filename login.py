from database import get_connection


def student_login():

    print("\n==============================")
    print("        STUDENT LOGIN")
    print("==============================")

    email = input("Enter email: ")
    password = input("Enter password: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT student_id, full_name
        FROM students
        WHERE email = %s AND password = %s
    """

    cursor.execute(
        query,
        (email, password)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    if student:

        print("\nLogin successful!")
        print("Welcome,", student[1])

        from students.dashboard import student_dashboard

        student_dashboard(
            student[0],
            student[1]
        )

    else:

        print("\nInvalid email or password.")
