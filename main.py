from pprint import pprint
import info
import utilities


main_menu = True
app = True
username = None
while app:
    print(info.main_menu)
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

                if utilities.check_status(user_login):
                    if utilities.login(user_login, user_password):
                        username = user_login
                        main_menu = False
                        print(info.user_menu)
                        print(f"Hello, {username}!")
                        break
                    else:
                        print("Something is wrong! Try again!")
                else:
                    print("This account was deleted!")
                    break

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
                        print(info.user_menu)
                        print(f"Hello, {username}!")
                        break
                    else:
                        print('Passwords are not the same!')
                else:
                    print('This login is already exist!')

        elif command == "/help":
            print(info.main_menu)

        elif command == "/exit":
            print("Goodbye!")
            main_menu = False
            app = False
            break

        else:
            print("Write correct request!")

    while utilities.check_login(username):
        command = input("What do you want? - ")

        if command == "/page":
            pprint(utilities.page_info(username), indent=2)

        elif command == "/help":
            print(info.user_menu)

        elif command == "/sign_out":
            print(f"\nBye, {username}!")
            username = None
            main_menu = True
            break

        elif command == "/exit":
            print("Goodbye!")
            username = None
            app = False
            break

        elif command == "/delete":
            while True:
                del_password = input("Write password here - ")
                if del_password == "/return":
                    break
                if utilities.check_pass(username, del_password):
                    utilities.delete_profile(username, del_password)
                    print(f"Bye, {username}!")
                    username = None
                    main_menu = True
                    break
                else:
                    print("Incorrect! Try again")
        else:
            print("Write correct request!")