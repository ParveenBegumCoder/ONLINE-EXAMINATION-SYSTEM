from admin.login import admin_login
from students.registration import register_student
from students.login import student_login


def main():

    while True:

        print("\n")
        print("==========================================")
        print("       ONLINE EXAMINATION SYSTEM")
        print("==========================================")

        print("1. Admin Login")
        print("2. Student Registration")
        print("3. Student Login")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            admin_login()

        elif choice == "2":

            register_student()

        elif choice == "3":

            student_login()

        elif choice == "4":

            print("\nThank You For Using Online Examination System.")
            break

        else:

            print("\nInvalid choice.")


if __name__ == "__main__":
    main()