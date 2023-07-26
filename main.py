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

                if utilities.login(user_login, user_password):
                    username = user_login
                    main_menu = False
                    print(info.user_menu)
                    print(f"Hello, {username}!")
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

        elif command == "/post":
            user_post = input("Write title of your post - ")
            if utilities.get_post(username, user_post):
                post = utilities.get_post(username, user_post)
                print(f"\n{post['title']}   {post['date_od_create']}\n--{post['description']}\n")
            else:
                print("Post do not exist!")

        elif command == "/add_post":
            while True:
                title = input("Write title of your post - ")
                if title == "/return":
                    break
                description = input("Write text - ")
                if description == "/return":
                    break
                utilities.add_new_post(username, title, description)
                print("Your post was successfully added!")
                break

        elif command == "/all_posts":
            lst = utilities.all_posts(username)
            if lst:
                for i in lst:
                    print(f"\n{i[0]}-{i[1]}   {i[3]}\n  --{i[2]}")
                print()
            else:
                print("You don't have any posts yet!")

        elif command == "/remove_post":
            post_title = input('Write title of a post - ')
            if utilities.check_post(username, post_title):
                utilities.remove_post(username, post_title)
                print("Your post was successfully removed!")
            else:
                print("This post not found!")

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