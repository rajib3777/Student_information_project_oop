class studentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls,student):
        cls.__student_list.append(student)

    @classmethod
    def enroll_id(cls,student_id):
        for student in cls.__student_list:
            if student.get_student() == student_id:
                return student
        return None

    @classmethod
    def view_student(cls):
        for student in cls.__student_list:
            print(student.student_info())
        if not cls.__student_list:
            print("No student available...")




class Student:
    def __init__(self,student_id,name,department,_is_enrolled = False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self._is_enrolled = _is_enrolled

    def get_student(self):
        return self.__student_id

    @staticmethod
    def Create_student_database(student_id,name,department):
        student = Student(student_id,name,department)
        studentDatabase.add_student(student)
        return student
    
    def enroll_student(self):
        if self._is_enrolled :
            return f"student id-----> {self.__student_id} already enrolled"
        else:
            self._is_enrolled = True
            return f"student id----> {self.__student_id} is enrolled successfully"
        
    def drop_student(self):
        if self._is_enrolled :
            self._is_enrolled = False
            return f"studen is------> {self.__student_id} is dropped sucessfully"
        else:
            return f"student------> {self.__student_id} is not found"
        
    def student_info(self):
        return f'ID : {self.__student_id}, Name : {self.__name}, Department : {self.__department}, Enrolled : {self._is_enrolled}'

Student.Create_student_database(1003,'Rajibul Islam Shuvo','CSE')
Student.Create_student_database(1120,'Abrar Haque','Botany')
Student.Create_student_database(2033,'Asrar haque','Chemistry')
Student.Create_student_database(3022,'Adnan Ashraf','Library Menagement')
Student.Create_student_database(990,'Ayesha Akhter','CSE')

def main_menu():
        
    while True:
        print("\n_____STUDENT DATABASE MENU_______")
        print("1. View All students")
        print("2. Enroll Students")
        print("3. Drop Student")
        print("4. Exit")


        option = int(input("Choose (1 - 4) instead: "))


        if option == 1:
            studentDatabase.view_student()
        elif option == 2:
            unique_id = int(input("Enter Your UNique id : "))
            student = studentDatabase.enroll_id(unique_id)
            if student :
                print(student.enroll_student())
            else:
                print("Student not found")
        elif option == 3:
            unique_id = int(input("Enter Your UNique id : "))
            student = studentDatabase.enroll_id(unique_id)
            if student :
                print(student.drop_student())
            else:
                print("Student not found")
        elif option == 4:
            print("Need to get out from program")
            break
        else:
            print("Your information does not valid")


main_menu()
        
