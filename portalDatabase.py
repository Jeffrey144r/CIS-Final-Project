import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="teachers_portal",
                 user='root',
                 password='Migue9885@'):
                   #Here I added my information from mysql to connect to database
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)

            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def getAllStudents(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor();
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID, grade):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            add_student = "INSERT INTO students (studentName, enrolledInCourseID, grade) VALUES (%s, %s, %s)"
            values = (name, courseID, grade)
            cursor.execute(add_student, values)
            self.connection.commit()
            cursor.close()

    def addCourse(self, name):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            add_course = "INSERT INTO courses (courseName) VALUES (%s)"
            values = (name,)
            cursor.execute(add_course, values)
            self.connection.commit()
            cursor.close()

    def modifyGrade(self, studentID, grade):
        ''' Complete the method to update the grade of the student'''
        pass