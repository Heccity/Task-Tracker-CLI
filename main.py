import json

message = "Welcome to Task Tracker CLI"
# add a task
def add():
    user_input = input("Enter a task: ")
    user_description = input("Enter a description: ")
    with open("list.json", "r") as f:
        data = json.load(f)
        data["tasks"].append(user_input)
    with open("list.json", "w") as f:
        json.dump(data, f)
    return user_input, user_description

def status():
    pass
    
# update a task
def update():
    task_id = input("Enter task ID to update: ")
    new_task = input("Enter updated task: ")
    return task_id, new_task

def list_tasks():
    with open("list.json", "r") as f:
        data = json.load(f)
        print(data)

# delete a task
def delete():
    tasks_id = input("Enter task ID to delete: ")
    with open("list.json", "r") as f:
        data = json.load(f)
        data["tasks"] = [task for task in data["tasks"] if task != tasks_id]
        with open("list.json", "w") as f:
            json.dump(data, f)
   
def main():
    print(message)
    print("1: Add task")
    print("2: Update task")
    print("3: List tasks")
    print("4: Delete task")
    
    match input("Enter a command: "):
        case "1":
            add()
        case "2":
            update()
        case "3":
            list_tasks()
        case "4":
            delete()
        case _:
            print("Invalid command")

main()