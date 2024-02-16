from . import psql_connection

def get_tasks():
    all_tasks = psql_connection.get_query("SELECT * FROM task;")
    return all_tasks

def add_task(title, description, status="new"):
    query = f"INSERT INTO task (title, description, status) VALUES ('{title}', '{description}', '{status}');"
    psql_connection.exec_query(query)
    return "Task added!"

def delete_task(id):
    query = f"DELETE FROM task WHERE id = {id};"
    psql_connection.exec_query(query)
    return "Task deleted!"

def update_task(id, title, description, status):
    query = f"UPDATE task SET title = '{title}', description = '{description}', status = '{status}' WHERE id = {id};"
    psql_connection.exec_query(query)
    return "Task updated!"

def create_table():
    query = "CREATE TABLE IF NOT EXISTS task (id SERIAL PRIMARY KEY, title VARCHAR(100), description TEXT, status VARCHAR(20), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    psql_connection.exec_query(query)
    return "Table created!"

if __name__ == "__main__":
    print(get_tasks())