from dataclasses import dataclass

@dataclass
class ToDo:
    id: int
    title: str
    description: str
    completed: bool

def main():
    todo_tracker = ToDoTracker()
    todo_tracker.create_todo(ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False))
    todo_tracker.create_todo(ToDo(id=2, title="Buy vegetables", description="Buy vegetables", completed=False))
    todo_tracker.create_todo(ToDo(id=3, title="Buy fruits", description="Buy fruits", completed=False))
    print(todo_tracker.search_todos("groceries"))

class ToDoTracker:
    def __init__(self):
        self.todos: list[ToDo] = []

    def create_todo(self, todo: ToDo):
        self.todos.append(todo)
        return todo

    def read_todos(self):
        return self.todos

    def get_todo(self, index: int):
        return self.todos[index]

    def search_todos(self, query: str):
        return [todo for todo in self.todos if query in todo.title or query in todo.description]

    def update_todo(self, index: int, new_todo: ToDo):
        self.todos[index] = new_todo

    def delete_todo(self, index: int):
        self.todos.pop(index)