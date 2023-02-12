import os

tasks = [
    "Buy milk",
    "Walk the dog",
    "Pay the bills",
    "Call mom",
    "Finish the report"
]

def print_tasks():
    for i, task in enumerate(tasks):
        status = "[ ]"
        if task.startswith("[x]"):
            status = "[x]"
        print(f"{i + 1}. {status} {task[3:]}")

def toggle_task(index):
    if tasks[index].startswith("[x]"):
        tasks[index] = "[ ]" + tasks[index][3:]
    else:
        tasks[index] = "[x]" + tasks[index][3:]

while True:
    os.system('clear')
    print("TODO LIST\n")
    print_tasks()
    print("\nCommands: (a)dd, (t)oggle, (q)uit")
    command = input("> ").lower()

    if command == "a":
        task = input("New task: ")
        tasks.append("[ ]" + task)
    elif command == "t":
        index = int(input("Task number: ")) - 1
        toggle_task(index)
    elif command == "q":
        break
