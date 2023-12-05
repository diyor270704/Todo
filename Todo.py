import json
from json import JSONDecodeError


def get_all_todos():
    try:
        with open("todos.json") as f:
            all_todos: list = json.load(f)
            f.close()
        return all_todos
    except (JSONDecodeError, FileNotFoundError):
        with open("todos.json", 'w') as f:
            json.dump([], f, indent=4)
            f.close()
        with open("todos.json") as f:
            all_todos: list = json.load(f)
            f.close()
        return all_todos


class Todo:
    def __init__(self, text, expires_at, owner):
        self.text = text
        self.expires_at = expires_at
        self.owner = owner

    def get_into_json(self):
        todo = {
            'id': 1 if len(get_all_todos()) == 1 else len(get_all_todos()) + 1,
            'text': self.text,
            'expires_at': self.expires_at,
            'owner': self.owner
        }
        try:
            with open("todos.json") as f:
                all_todos: list = json.load(f)
                f.close()
            all_todos.append(todo)
            with open("todos.json", "w") as f:
                json.dump(all_todos, f, indent=4)
                f.close()
            print('added successfully :)')
        except (JSONDecodeError, FileNotFoundError):
            with open("todos.json", "w") as f:
                json.dump([], f, indent=4)
                f.close()
                with open("todos.json") as f:
                    all_todos: list = json.load(f)
                    f.close()
                all_todos.append(todo)
                with open("todos.json", "w") as f:
                    json.dump(all_todos, f, indent=4)
                    f.close()
                print('added successfully :)')
