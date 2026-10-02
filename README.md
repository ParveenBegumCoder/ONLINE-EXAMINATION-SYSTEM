# online-examination-system
Online Examination System using Python and MySQL
How to Run the Project

1. Clone the Repository

git clone https://github.com/ParveenBegumCoder/online-examination-system.git

Go to the project folder:

cd ONLINE-EXAMINATION-SYSTEM

2. Install Required Python Packages

Install the packages from "requirements.txt":

pip install -r requirements.txt

3. Set Up MySQL Database

1. Open MySQL / MySQL Workbench.
2. Create the project database.
3. Create the required tables.
4. Update the MySQL username, password and database name in "database.py".

Example:

host = "localhost"
user = "root"
password = "your_mysql_password"
database = "ONLINE_EXAMINATION_SYSTEM"

4. Run the Application

From the main project folder, run:

python main.py

5. Use the Application

**The main menu provides options such as:**

- Admin Login
- Student Registration
- Student Login
- Online Examination
- View Results

**Requirements**

- Python 3.x
- MySQL Server
- MySQL Workbench (optional)
- Required Python packages listed in "requirements.txt"
