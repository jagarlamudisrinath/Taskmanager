from . import psql_connection

def get_tasks():
    all_tasks = psql_connection.get_query("SELECT * FROM task;")
    return all_tasks

def add_task(name, description, status="new"):
    query = f"INSERT INTO task (title, description, status) VALUES ('{name}', '{description}', '{status}');"
    psql_connection.exec_query(query)
    return "Task added!"

def delete_task(id):
    query = f"DELETE FROM task WHERE id = {id};"
    psql_connection.exec_query(query)
    return "Task deleted!"

def update_task(id, name, description, status):
    query = f"UPDATE task SET title = '{name}', description = '{description}', status = '{status}' WHERE id = {id};"
    psql_connection.exec_query(query)
    return "Task updated!"


if __name__ == "__main__":
    print(get_tasks())
    print(add_task("Task 1", "This is task 1"), "new")
    # print(delete_task(1))
    # print(update_task(2, "Task 2", "This is task 2"))