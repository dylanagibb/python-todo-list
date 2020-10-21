class ToDoItem:
    key = ""
    title = ""
    description = ""
    done = False

    def load_item(self, item_key, item_data):
        self.key = item_key
        self.title = item_data['title']
        self.description = item_data['description']
        self.done = item_data['done']

    def print_item(self):
        print("%s\t%s" % (self.title, self.done))