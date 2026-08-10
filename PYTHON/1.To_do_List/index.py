tasks = []

def add_task():
    task = input("Enter Your Task: ")
    tasks.append(task)
    print("Task is Added SuccessFully...")
    
def view_task():
    print("\n ---------See Your Tasks -----------")
    
    if len(tasks) == 0:
        print("No tasks is Added")
        
    else:
        for i , task in enumerate(tasks, start=1):
            print(i ,task)
            

def delete_task():
    view_task()
    
    try:
        task_number = int(input("Enter your number: "))
        
        if task_number < 1 or task_number>len(tasks):
            print("Invalid Task number...")
            
        else:
            tasks.pop(task_number -1)
            print("deleted Successfully....")
            
    except ValueError:
        print("Please Enter number...")
        
def update_task():
    view_task()
    
    try:
        task_number=int(input("Enter task number to update: "))
        
        if task_number < 1 or task_number > len(tasks):
            print("Invalid number")
        else:
            new_task = input("Enter New task: ")
            tasks[task_number-1] = new_task
            print("Task updated Successfully...")
    
    except ValueError:
        print("Please Enter a number")
    
while True:
    print("\n----------TO-DO-LIST-------------")
    print("1. Add Task")
    print("2. View task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter Your choice: ")
    
    if choice == "1":
        add_task()
        
    elif choice == "2":
        view_task()
        
    elif choice == "3":
        delete_task()
    
    elif choice == "4":
        update_task()
            
    elif choice == "5":
        print("Thank You.......")
        break
    
    else:
        print("Invalid Choice")