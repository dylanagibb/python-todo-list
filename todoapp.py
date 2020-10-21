import json
from whaaaaat import prompt, print_json 
from todolist import ToDoList

#using_app = True
active_list = ToDoList()

def main():
    questions = [
        {
            'type': 'input',
            'name': 'first_name',
            'message': 'What\'s your first name'
        }
    ]

    answers = prompt(questions)
    print_json(answers)

if __name__ == "__main__":
    main()

#with open('todolist.json') as todo_list_json:
#    todo_list_dictionary = json.load(todo_list_json)

#while using_app:
#    for todo_list in todo_list_dictionary.items():
#        user_input = int(input("Which list would you like to load?"))
#        if user_input is 0:
#            using_app = False
#        elif user_input is 1:
#            print("loading list...")
#            active_list.load_todo_list(todo_list)