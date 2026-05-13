from dataclasses import dataclass


@dataclass
class ToDo:
    id: int
    title: str
    description: str
    completed: bool


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


def main():
    tracker = ToDoTracker()
    tracker.create_todo(
        ToDo(id=1, title="Buy groceries", description="weekly run", completed=False)
    )
    tracker.create_todo(
        ToDo(id=2, title="Buy vegetables", description="for the soup", completed=False)
    )
    tracker.create_todo(
        ToDo(id=3, title="Buy fruits", description="bananas + apples", completed=False)
    )
    print(tracker.search_todos("groceries"))


if __name__ == "__main__":
    main()
