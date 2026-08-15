import oracledb
from db import get_connection

def add_emp():
    connection = get_connection()
    
    if connection:
        try:
            emp_id = int(input("Enter Employee_id: ")) 
            emp_name = input("Enter Employee Name: ")
            emp_age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            job_role = input("Enter Job Role: ")
            salary = int(input("Enter Salary: "))
            
            cursor = connection.cursor()
            cursor.execute("""insert into employees(emp_id,emp_name,emp_age,department,job_role,salary)
                           values(:1, :2, :3, :4, :5, :6)""",[emp_id,emp_name,emp_age,department,job_role,salary])
            
            connection.commit()
            
            print("Employees Details Added Successfully......")
            
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ", e)
        except ValueError:
            print("Invalid Details.....")
# add_emp()

def view_emp():
    connection = get_connection()
    
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""select emp_id,emp_name,emp_age,department,job_role,salary
                           from employees
                           order by emp_id""")
            
            employees = cursor.fetchall()
            
            if employees:
                print("---/n All Employees Details--------")
                
                for i in employees:
                    print("emp_id: ",i[0])
                    print("emp_name: ",i[1])
                    print("emp_age: ",i[2])
                    print("Department: ",i[3])
                    print("Job_Role: ",i[4])
                    print("salary: ",i[5])
                    
            else:
                print("No Records were Found")
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ",e)
            
        except ValueError:
            print("Invalid Details....")
            
# view_emp()

def search_emp():
    connection = get_connection()
    
    if connection:
        try:
            emp_id = int(input("Enter Employee_ Id to serach: "))
            
            cursor = connection.cursor()
            cursor.execute("""select emp_id,emp_name,emp_age,department,job_role,salary
                           from employees
                           where emp_id = :1""",[emp_id])
            
            employee = cursor.fetchone()
            
            if employee:
                print("-----------/n Search Employee Id ----------")
                print("emp_id: ",employee[0])
                print("emp_name: ",employee[1])
                print("emp_age: ",employee[2])
                print("department: ",employee[3])
                print("job_role: ",employee[4])
                print("salary: ",employee[5])
            
            else:
                print("Employee Not Found.........")
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ",e)
        
        except ValueError:
            print("Invalid Details.......")
            
# search_emp()

def update_emp():
    connection = get_connection()
    
    if connection:
        try:
            emp_id = int(input("Enter Student_id to update: "))
            
            cursor = connection.cursor()
            cursor.execute("""select emp_id,emp_name,emp_age,department,job_role,salary
                           from employees
                           where emp_id = :1""",[emp_id])
            
            
            employee = cursor.fetchone()
            
            if employee:
                print("---\n Update Details of Employees-----")
                print("emp_name: ",employee[1])
                print("emp_age: ",employee[2])
                print("department: ",employee[3])
                print("job_role: ",employee[4])
                print("salary: ",employee[5])
                
                name = input("Enter New Employee Name: ")
                age = int(input("Enter Employee Age: "))
                Dept = input("Enter Department: ")
                jobRole = input("Enter Job Role of Employee: ")
                Salary = int(input("Enter salary: "))
                
                cursor.execute("""update employees
                               set emp_name = :1,
                               emp_age = :2,
                               department = :3,
                               job_role = :4,
                               salary = :5
                               where emp_id = :6""",[name,age,Dept,jobRole,Salary,emp_id])
                
                connection.commit()
                print("Updated Successfully..........")
                
            else:
                print("Not Updated........")
                
                
            cursor.close()
            connection.close()
                
        except oracledb.Error as e:
            print("Error: ", e)  
        
        except ValueError:
            print("Invalid Details...")
            
# update_emp()

def delete_emp():
    connection = get_connection()
    
    if connection:
        try:
            emp_id = int(input("Enter employee Id to delete: "))
            
            cursor = connection.cursor()
            cursor.execute("""select emp_id,emp_name
                           from employees
                           where emp_id = :1""",[emp_id])
            
            employee = cursor.fetchone()
            
            if employee:
                print("------\n Student Found-----")
                print("ID: ", employee[0])
                print("name: ", employee[1])
                
                confirm = input("Are U sure u want to delete (yes/no): ").lower()
                if confirm == "yes":
                    cursor.execute("""delete from employees
                                   where emp_id = :1 """,[emp_id])
                    
                    connection.commit()
                    print("Employee details Deleted SuccessFully......")
                    
                else:
                    print("No Records were Found.......")
                    
            else:
                print("Student not Found....")
                
            cursor.close()
            connection.close()
            
        except oracledb.Error as e:
            print("Error: ",e)
            
        
        except ValueError:
            print("Invalid Details........")
            
# delete_emp()

def main():
    while True:
        print("--------------------\n EMPLOYEES MANAGEMENT SYSTEM--------------------------- ")
        print()
    
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4, Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Enter Your Choice: ")
        
        if choice == "1":
            add_emp()
            
        elif choice == "2":
            view_emp()
            
        elif choice == "3":
            search_emp()
            
        elif choice == "4":
            update_emp()
            
        elif choice == "5":
            delete_emp()
            
        elif choice == "6":
            print("Thank You For yur Time..............")
            break
        
        else:
            print("Please Enter Valide Number....")
            
main()
            
    