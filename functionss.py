import json
from Todo import Todo, get_all_todos

def add_todo(userid):
    text = input("enter text todo: ")
    expires_at = input("enter when it will be expired at 'hh-mm-ss'")
    todo_obj = Todo(text, expires_at, userid)
    todo_obj.get_into_json()
    all_todos = get_all_todos()
    for i in all_todos:
        if i['text'] == text and i['expires_at'] == expires_at:
            return i['id']

def delete_todo():
    todo_id = int(input("enter your todo's id to delete: "))
    all_todos = get_all_todos()
    for t in all_todos:
        if t['id'] == todo_id:
            all_todos.remove(t)
    with open("todos.json", "w") as f:
        json.dump(all_todos, f, indent=4)
        f.close()

def change_todo():
    todo_id = int(input("enter your todo's id to delete: "))
    all_todos = get_all_todos()
    for t in all_todos:
        if t['id'] == todo_id:
            print("your todo text is", t['text'])
            print("your todo expires at", t['expires_at'])
            text = input("enter changes to your todo: ")
            expires_at = input("enter changed time to your todo hh-mm-ss: ")
            t['text'] = text
            t['expires_at'] = expires_at

    with open("todos.json", "w") as f:
        json.dump(all_todos, f, indent=4)
        f.close()



