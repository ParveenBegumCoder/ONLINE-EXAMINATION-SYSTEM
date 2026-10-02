from database import get_connection
from students.exam import start_exam


def view_subjects():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject_id, subject_name
        FROM subjects
    """)

    subjects = cursor.fetchall()

    print("\n========== AVAILABLE SUBJECTS ==========")

    for subject in subjects:
        print(
            f"{subject[0]}. {subject[1]}"
        )

    cursor.close()
    connection.close()

    return subjects


def view_results(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            sub.subject_name,
            r.total_questions,
            r.correct_answers,
            r.score,
            r.exam_date

        FROM results r

        INNER JOIN subjects sub
        ON r.subject_id = sub.subject_id

        WHERE r.student_id = %s

        ORDER BY r.exam_date DESC
    """

    cursor.execute(query, (student_id,))

    results = cursor.fetchall()

    print("\n========== MY RESULTS ==========")

    if not results:
        print("No examination results found.")

    for result in results:

        print("\nSubject:", result[0])
        print("Total Questions:", result[1])
        print("Correct Answers:", result[2])
        print("Score:", result[3])
        print("Date:", result[4])

    cursor.close()
    connection.close()


def student_dashboard(student_id, student_name):

    while True:

        print("\n================================")
        print("       STUDENT DASHBOARD")
        print("================================")

        print("Student:", student_name)

        print("\n1. View Subjects")
        print("2. Start Examination")
        print("3. View My Results")
        print("4. Logout")

        choice = input("\nEnter choice: ")

        if choice == "1":

            view_subjects()

        elif choice == "2":

            subjects = view_subjects()

            if subjects:

                try:
                    subject_id = int(
                        input(
                            "\nEnter subject ID: "
                        )
                    )

                    start_exam(
                        student_id,
                        subject_id
                    )

                except ValueError:

                    print("Invalid subject ID.")

        elif choice == "3":

            view_results(student_id)

        elif choice == "4":

            print("Student logged out.")
            break

        else:

            print("Invalid choice.")
