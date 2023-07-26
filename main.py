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

    elif command == "/register":
        while True:
            reg_login = input("Write your new login - ")
            if reg_login == '/return':
                break
            reg_password = input("Write your new password - ")
            if reg_password == '/return':
                break
            reg_second_password = input("Write your new password again - ")
            if reg_second_password == '/return':
                break

            if not utilities.check_login(reg_login):
                if reg_password == reg_second_password:
                    utilities.register(reg_login, reg_password)
                    print('You are successfully sign in!')
                    main_menu = False
                    username = reg_login
                    break
                else:
                    print('Passwords are not the same!')
            else:
                print('This login is already exist!')

    elif command == "/help":
        print(info.main_menu)

    elif command == "/exit":
        print("Goodbye!")
        break

    else:
        print("Write correct request!")