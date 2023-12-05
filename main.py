from register_and_login import register, login
from functionss import add_todo, delete_todo, change_todo

print("welcome to our Todo app :)")
check = int(input("1 = register\n2 = login"))
k = 0
l = 0
if check == 1:
    if register():
        k += 1
if check == 2 or k == 1:
    l = login()
    if l != 0:
        print("you logged in now you can add, delete, change Todos")
        check_t = int(input("1 = add todos\n2 = delete todos\n3 = change todos"))
        if check_t == 1:
            d = add_todo(l)
            print(f"your todo's id is{d} you need this id to delete and change your todo")
        if check_t == 2:
            delete_todo()
        if check_t == 3:
            change_todo()
    else:
        print("username or password incorrect")
