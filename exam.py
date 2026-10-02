from database import get_connection


def start_exam(student_id, subject_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            question_id,
            question_text,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer
        FROM questions
        WHERE subject_id = %s
    """

    cursor.execute(query, (subject_id,))

    questions = cursor.fetchall()

    if not questions:

        print("\nNo questions available for this subject.")

        cursor.close()
        connection.close()

        return

    print("\n================================")
    print("       ONLINE EXAMINATION")
    print("================================")

    print("Total Questions:", len(questions))

    input("\nPress ENTER to start the examination...")

    correct_count = 0

    answers = []

    for number, question in enumerate(
        questions,
        start=1
    ):

        print("\n--------------------------------")
        print(
            f"Question {number} "
            f"of {len(questions)}"
        )

        print(question["question_text"])

        print("A.", question["option_a"])
        print("B.", question["option_b"])
        print("C.", question["option_c"])
        print("D.", question["option_d"])

        while True:

            selected = input(
                "Enter your answer (A/B/C/D): "
            ).upper()

            if selected in ["A", "B", "C", "D"]:
                break

            print("Please enter A, B, C or D.")

        is_correct = (
            selected ==
            question["correct_answer"]
        )

        if is_correct:
            correct_count += 1

        answers.append(
            (
                question["question_id"],
                selected,
                is_correct
            )
        )

    total_questions = len(questions)

    score = (
        correct_count /
        total_questions
    ) * 100

    # Create exam record

    cursor.execute(
        """
        INSERT INTO exams
        (student_id, subject_id)
        VALUES (%s, %s)
        """,
        (student_id, subject_id)
    )

    exam_id = cursor.lastrowid

    # Store answers

    for question_id, selected, is_correct in answers:

        cursor.execute(
            """
            INSERT INTO answers
            (
                exam_id,
                question_id,
                selected_answer,
                is_correct
            )
            VALUES (%s, %s, %s, %s)
            """,
            (
                exam_id,
                question_id,
                selected,
                is_correct
            )
        )

    # Store result

    cursor.execute(
        """
        INSERT INTO results
        (
            exam_id,
            student_id,
            subject_id,
            total_questions,
            correct_answers,
            score
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            exam_id,
            student_id,
            subject_id,
            total_questions,
            correct_count,
            score
        )
    )

    connection.commit()

    print("\n================================")
    print("       EXAM COMPLETED")
    print("================================")

    print("Total Questions:", total_questions)
    print("Correct Answers:", correct_count)
    print("Wrong Answers:", total_questions - correct_count)
    print("Score:", round(score, 2), "%")

    if score >= 40:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    cursor.close()
    connection.close()
