import webbrowser
import json
import os
import time
#database
tasks=[{"name":"", "is_done": False}]
tasks_list= 'tasks_list.json'
if os.path.exists(tasks_list):
    with open(tasks_list, "r") as f:
        content = f.read()
        if content:
            tasks = json.loads(content)
        else:
            tasks=[]
else:
    tasks=[] # bro said no comment
url = 'https://www.youtube.com/watch?v=KxGRhd_iWuE' # I guess we will never know -Kanye West

def options():
    print(
        "\n"
        "rand_quote_that_doesnt_make_sense() \n\n"
        "[n] [option]\n\n"
        "[1] Show tasks \n"
        "[2] Edit tasks\n"
        "[3] Remaining tasks\n"
        "[4] Done tasks\n"
        "[5] I am cooked" 
        "\n"
    )
    global option_input
    option_input = (input("Just paste a number, nothing else: "))
    
    
def show_tasks():
    print("\n")
    if tasks==[]:
        print(
            "Start by adding a tasks through edit tasks"
        )
    for i,task in enumerate(tasks, start=1):
        status = "✓" if task["is_done"] else "X"
        print(f"[{i}][{status}] {task["name"]}")
    print("\n")

def edit_tasks():
    print(
           "\n"
           "[n] [option]\n\n"
           "[1] Add tasks\n"
           "[2] Delete tasks\n"
           "[3] Mark a task as done\n"
           "[4] Mark task as remain" 
           "\n"
       )
    global edit_tasks_input
    edit_tasks_input = input("Another one: ")
edit_tasks_input="" 
def iam_cooked():
    webbrowser.open(url) 
    
#edit options-------
def add_tasks():
    while True:
        show_tasks()
        add_task=input("Add task or enter 2 to exit: ")
        if add_task == '2':
            break
        tasks.append({"name": add_task, "is_done": False}) 
def done_tasks():
    print ("\n")
    for i , task in enumerate(tasks, start=1):
        if task["is_done"] == True:
            print(f"[{i}] {task["name"]} \n")
def remain_tasks():
    print ("\n")
    for i, task in enumerate(tasks, start=1):
        if task["is_done"] == False:
            print(f"[{i}]{task["name"]} \n")
        
def del_tasks():
    while True:
        show_tasks()
        choice= input("Enter the number of the task to delete or e to exit: " )
        if choice.lower() == 'e':
            break
        try:
            number = int(choice)
        except ValueError:
            print("\n !!!!!!!You blind bro? thats not a number!!!!!!! \n" ) 
            time.sleep(0.5)
            continue
        if number < 0 or number > len(tasks): 
            print("\n !!!!!!!Put a valid number blyat!!!!!!! \n")
            time.sleep(0.5)
            continue
        tasks.pop(int(choice)-1)

def markDone_task():
    while True:
        remain_tasks()
        choice= input("Enter the number of the task to delete or e to exit: " )
        if choice.lower() == 'e':
            break
        try:
            number = int(choice)
        except ValueError:
            print("\n !!!!!!!You blind bro? thats not a number!!!!!!! \n" ) 
            time.sleep(0.5)
            continue
        if number < 0 or number > len(tasks): 
            print("\n !!!!!!!Put a valid number blyat!!!!!!! \n")
            time.sleep(0.5)
            continue
        tasks[number-1]["is_done"] = not tasks[number-1]["is_done"]
        
def markRemain_task():
    while True:
        done_tasks()
        choice= input("Enter the number of the task to delete or e to exit: " )
        if choice.lower() == 'e':
            break
        try:
            number = int(choice)
        except ValueError:
            print("\n !!!!!!!You blind bro? thats not a number!!!!!!! \n" ) 
            time.sleep(0.5)
            continue
        if number < 0 or number > len(tasks): 
            print("\n !!!!!!!Put a valid number blyat!!!!!!! \n")
            time.sleep(0.5)
            continue
        tasks[number-1]["is_done"] = not tasks[number-1]["is_done"]
       
    
#executions
options()

       
match option_input: #ignore the pylance here because it sucks
    case '1':
        show_tasks()
    case '2':
        edit_tasks()
    case '3':
        remain_tasks()
    case '4':
        done_tasks()
    case '5':
        iam_cooked()
    case _:
        print("Insert a valid number bud")

match edit_tasks_input:
    case '1':
         add_tasks()
    case '2':
        del_tasks()
    case '3':
        markDone_task()
    case '4':
        markRemain_task()
    
#executions#
with open(tasks_list, "w") as f:
    json.dump(tasks, f)
