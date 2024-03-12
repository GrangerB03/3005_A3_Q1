import psycopg2 as db
import datetime

#change this to your password
PASSWORD = "password123"
DATABASE_NAME = "database1"

#contant for the menu text
MENU_TEXT = "Select an opertion (q to quit):\n1. getAllStudents\n2. addStudent\n3. updateStudentEmail\n4. deleteStudent\n"

#connect to database
connection = db.connect(database = DATABASE_NAME, user = "postgres", host = "localhost", password = PASSWORD, port = 5432)

#open a cursor to perform operations
app = connection.cursor()

#functions for each of the operations

def getAllStudents():
    #select all query
    app.execute("SELECT * FROM students ORDER BY student_id asc")
    rows = app.fetchall()
    
    for row in rows:
        print(row)

def addStudent():
    #get input values
    print("\n")
    firstName = input("Input the value for the first_name column: ")
    lastName = input("Input the value for the last_name column: ")
    email = input("Input the value for the email column: ")
    year = int(input("Input the value for the enrollment_date column's year: "))
    month = int(input("Input the value for the enrollment_date column's month: "))
    day = int(input("Input the value for the enrollment_date column's day: "))
    
    date = datetime.datetime(year, month, day)
    
    #perform query
    app.execute("INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES ('" + firstName + "', '" + lastName + "', '" + email + "', '" + str(date) + "')")
    connection.commit()


def updateStudentEmail():
    #get input values
    print("\n")
    id = int(input("Input the student_id value of the student: "))
    email = input("Input the new email: ")
    
    #perform query
    app.execute("UPDATE students SET email = '" + email + "' WHERE student_id = " + str(id))
    connection.commit()
    

def deleteStudent():
    #get input values
    print("\n")
    id = int(input("Input the student_id value for the student to be deleted: "))
    
    #perform query
    app.execute("DELETE FROM students WHERE student_id = " + str(id))
    connection.commit()

def menu():
    while 1:
        value = input(MENU_TEXT)
        
        #quit check
        if(value == 'q' or value == 'Q'):
            return
        
        #switch for valid inputs
        match value:
            case '1':
                getAllStudents()
            case '2':
                addStudent()
            case '3':
                updateStudentEmail()
            case '4':
                deleteStudent()
            case _:
                print("Invalid input")
                continue
        print("\n")

menu()
#close connection
app.close()
connection.close()