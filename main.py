import info
import utilities


print(info.main_menu)
main_menu = True
username = None

while main_menu:
    command = input("What do you want today? - ")

    if command == "/login":
        while True:
            user_login = input("\nWrite your login - ")
            if user_login == "/return":
                break
            user_password = input("Write your password - ")
            if user_password == '/return':
                break

            if utilities.login(user_login, user_password):
                username = user_login
                main_menu = False
                break
            else:
                print("Something is wrong! Try again!")

    elif command == "/help":
        print(info.main_menu)

    elif command == "/exit":
        print("Goodbye!")
        break

    else:
        print("Write correct request!")

print(f"\nWelcome back, {username}")