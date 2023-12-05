from User import User, get_data


def register():
    name = input("enter your name: ")
    lastname = input("enter your lastname: ")
    email = input("enter your email address: ")
    username = input("enter username: ")
    password = input("enter password: ")
    user_obj = User(name, lastname, email, username, password)
    user_obj.set_into_json()
    return True


def login():
    username = input("enter your username: ")
    password = input("enter your password: ")
    all_users = get_data()
    for user in all_users:
        if user['username'] == username and user['password'] == password:
            return user['id']
        else:
            return 0
