from db import get_connection


# =========================
# ADD TASK
# =========================

def add_task():

    task_name = input("Enter task: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO tasks (task_name)
        VALUES (:task_name)
    """

    cursor.execute(
        query,
        task_name=task_name
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Task added successfully!")


# =========================
# VIEW TASKS
# =========================

def view_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT task_id, task_name
        FROM tasks
        ORDER BY task_id
    """

    cursor.execute(query)

    tasks = cursor.fetchall()

    print("\n========== TASKS ==========")

    if len(tasks) == 0:
        print("No tasks found.")

    else:
        for task in tasks:
            print(task[0], "-", task[1])

    cursor.close()
    connection.close()


# =========================
# UPDATE TASK
# =========================

def update_task():

    task_id = int(input("Enter task ID to update: "))
    new_task = input("Enter new task: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE tasks
        SET task_name = :new_task
        WHERE task_id = :task_id
    """

    cursor.execute(
        query,
        new_task=new_task,
        task_id=task_id
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Task updated successfully!")
    else:
        print("Task not found!")

    cursor.close()
    connection.close()


# =========================
# DELETE TASK
# =========================

def delete_task():

    task_id = int(input("Enter task ID to delete: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM tasks
        WHERE task_id = :task_id
    """

    cursor.execute(
        query,
        task_id=task_id
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Task deleted successfully!")
    else:
        print("Task not found!")

    cursor.close()
    connection.close()


# =========================
# MAIN MENU
# =========================

while True:

    print("\n========== TO-DO LIST ==========")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        update_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        print("Thank you for using To-Do List!")
        break

    else:

        print("Invalid choice!")