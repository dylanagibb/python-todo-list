from todoitem import ToDoItem

class ToDoList:
    todo_items = []

    def load_todo_list(self, todo_list_dictionary):
        for item_key, item_data in todo_list_dictionary[1]['items'].items():
            todo_item = ToDoItem()
            todo_item.load_item(item_key, item_data)
            self.todo_items.append(todo_item)

        for item in self.todo_items: item.print_item()

    #def update_todolist(self,todo_item):
    #    with open('todolist.json', 'r') as todo_list_json:
    #        data = json.load(todo_list_json)

    #    data['work-todo']['items'][todo_item]['done'] = True

    #    with open('todolist.json', 'w') as todo_list_json:
    #        json.dump(data, todo_list_json)