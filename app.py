from flask import Flask, request, render_template
from utils import psql_connection, tasks
import logging

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/get-tasks")
def get_tasks():
    all_tasks = tasks.get_tasks()
    return all_tasks

@app.route("/add-task", methods=["POST"])
def add_task():
    name = request.form["name"]
    description = request.form["description"]
    return tasks.add_task(name, description)

@app.route("/delete-task", methods=["DELETE"])
def delete_task():
    id = request.form["id"]
    return tasks.delete_task(id)

@app.route("/update-task", methods=["PUT"])
def update_task():
    id = request.form["id"]
    name = request.form["name"]
    description = request.form["description"]
    status = request.form["status"]
    return tasks.update_task(id, name, description, status)



if __name__ == "__main__":
    app.run(debug=True, port=8000)