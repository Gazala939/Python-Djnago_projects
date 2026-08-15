import oracledb
from db import get_connection

def add_student():
    connection = get_connection()
    
    if connection:
        try:
            
            stu_id = int(input("Enter Student_ID: "))
            stu_name = input("Enter Student name: ")
            stu_age = int(input("Enter Student Age: "))
            course = input("Enter Course Name: ")
            marks = int(input("Enter Student marks: "))
            
            
            cursor = connection.cursor()
            cursor.execute("""insert into students(stu_id,stu_name,stu_age,course,marks)
                           values(:1, :2, :3, :4, :5)""",[stu_id,stu_name,stu_age,course,marks])
            
            connection.commit()
            print("Students Details Added Successfully.....")
            
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error, e") 
        
        except ValueError:
            print("Invalid Details")
            
# add_student()

def view_students():
    connection = get_connection()
    
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(""" select stu_id,stu_name,stu_age,course,marks
                           from students
                           order by stu_id""")
            
            students = cursor.fetchall()
            
            if students:
                print("\n ------------All Students Records--------------")
                for i in students:
                    print("Student_id: ", i[0])
                    print("Student_name: ", i[1])
                    print("Student_age: ", i[2])
                    print("Course: ", i[3])
                    print("Marks: ", i[4])
            else:
                print("No students Records were Found......")
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ", e)
            
        except ValueError:
            print("Please Enter valid Details")
            
# view_students()

def search_student():
    connection = get_connection()
    
    if connection:
        try:
            stu_id = int(input("Enter Student_Id: "))
            cursor = connection.cursor()
            cursor.execute("""select stu_id,stu_name,stu_age,course,marks
                           from students
                           where stu_id = :1""",[stu_id])
            
            student = cursor.fetchone()
            
            if student:
                print("----------/nStudent u have Searched----------------")
                
                print("Student_id: ", student[0])
                print("Student_name: ", student[1])
                print("Student_age: ", student[2])
                print("Course: ", student[3])
                print("Marks: ", student[4])
            else:
                print("Student Id was Not Found")      
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ",e)
            
        except ValueError:
            print("Invalid Details.....")
            
# search_student()

def update_student():
    connection = get_connection()
    if connection:
        try:
            stu_id = int(input("Enter Student_Id to Update: "))
            cursor = connection.cursor()
            cursor.execute("""select stu_id,stu_name,stu_age,course,marks
                           from students
                           where stu_id = :1""",[stu_id])
            
            student = cursor.fetchone()
            
            if student:
                print("---------/n Update Student Record----------")
                print("Student_name: ", student[1])
                print("Student_age: ", student[2])
                print("Course: ", student[3])
                print("Marks: ", student[4])
                
                
                
                name = input("Enter new name: ")
                age = int(input("Enter Age: "))
                Course = input("Enter Course name: ")
                Marks = int(input("Enter Marks: "))
            
                cursor.execute("""update students
                               set
                               stu_name = :1,
                               stu_age = :2,
                               course = :3,
                               marks = :4
                               where stu_id = :5""",[name,age,Course,Marks,stu_id])
            
                connection.commit()
                print("/n Student Update Successfully......")
            else:
                print("Student not found.......")
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ",e)
            
                
        except ValueError():
            print("Invalid Details....")
            
# update_student()

def delete_student():
    connection = get_connection()
    
    if connection:
        try:
            stu_id = int(input("Enter stu_id to delete...."))
            cursor = connection.cursor()
            cursor.execute("""select stu_id,stu_age
                           from students
                           where stu_id = :1""",[stu_id])
            
            student = cursor.fetchone()
            
            if student:
                print("-------/nStudent Found-------")
                print("Stu_Id: ",student[0])
                print("Name: ",student[1])
                
                confirm = input("Are u sure u want to delete (yes/no): ").lower()
                if confirm == "yes":
                    cursor.execute("""delete from students
                    where stu_id = :1""",[stu_id])
                    connection.commit()
                    print("Student Delete Successfully.....")
                
                else:
                    print("Delete Operation Cancelled.....")
            else:
                print("Student Record Not Found........")
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ", e)
        except ValueError:
            print("Invalid Details.........")
            
# delete_student()
def main():
    while True:
        print("---------------/n STUDENT MANAGEMENT RECORD--------------------------")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. EXIT")
        
        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_student()
        
        elif choice == "2":
            view_students()
        
        elif choice == "3":
            search_student()
        
        elif choice == "4":
            update_student()
        
        elif choice == "5":
            delete_student()
        
        elif choice == "6":
            print("ThankYou...............")
            break
    
        else:
            print("Invalid Choice........")
            
main()