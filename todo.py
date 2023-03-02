class Todo:
    def __init__(self, code_id: int, title: str, description: str):

        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed = False
        self.tags: list = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos = {}

    def add_todo(self, title: str, description: str):

        id = len(self.todos) + 1

        todo = Todo(id, title, description)

        self.todos[id] = todo

        return id

    def pending_todos(self):
        lista_pending = [todo for todo in self.todos.values() if todo.completed is False]
        return lista_pending

    def completed_todos(self):
        lista_pending = [todo for todo in self.todos.values() if todo.completed is True]
        return lista_pending

    def tags_todo_count(self):
        todo_dict = {}
        for todo in self.todos.values():
            for todo in self.todos.tags():
                if


        return

