import psycopg2
import datetime


conn = psycopg2.connect(dbname="loginpasswordsql", user="cer6erus7")
cur = conn.cursor()

def login(login, password):
    """
    Принимает логин и пароль пользователя. Делает запрос в базу данных postgreSQL и запрашивает данные введенные
    пользователем, если же эти данные существуют и совпадают с пользовательскими, функция возвращает истинну, если
    же не совпадают, ложь
    :param login:
    :param password:
    :return:
    """
    cur.execute(f"SELECT username, password FROM users WHERE username = '{login}' AND status = 1")
    result = cur.fetchall()
    try:
        if result[0][0] == login and result[0][1] == password:
            return True
        else:
            return False
    except:
        return False


def check_login(login):
    """
    Принимает логин и просматривает его в базе данных. Если такой лонин существует, возвращает значение True, если
    же нет возвращает False.
    :param login:
    :return:
    """
    cur.execute(f"SELECT username FROM users WHERE username = '{login}'")
    if cur.fetchall():
        return True
    else:
        return False


def register(login, password):
    """
    Принимает логин и пароль пользователя и создает новый профиль в базе данных;
    :param login:
    :param password:
    :return:
    """
    time = datetime.datetime.now()
    cur.execute(f"INSERT INTO users (username, password, date_of_create, status) VALUES ('{login}', '{password}', '{time}', 1);")
    conn.commit()


def page_info(login):
    """
    Сериализуем данные полученные в базе данных и выводим их в виде словаря
    :param login:
    :return:
    """
    cur.execute(f"SELECT user_id, username, date_of_create, status FROM users WHERE username = '{login}'")
    result = cur.fetchall()
    time = result[0][2]
    return {"user_id": result[0][0], "username": result[0][1], "date_of_create": time.strftime("%d-%m-%y %H:%M:%S"), "status": result[0][3]}


def check_pass(login, password):
    """
    Проверяет логин и пароль, и возвращает True если они совпадают с данныеми в базе данных, или же False
    :param login:
    :param password:
    :return:
    """
    cur.execute(f"SELECT username, password FROM users WHERE username = '{login}' AND password = '{password}'")
    if cur.fetchall():
        return True
    else:
        return False


def delete_profile(login, password):
    """
    Меняем статус на неактивный в базе данных
    :param login:
    :param password:
    :return:
    """
    cur.execute(f"UPDATE users SET status = 0 WHERE username = '{login}' AND password = '{password}'")
    conn.commit()


def get_post(login, title):
    """
    Принимает логин и пароль пользователя, делает запрос в базу данных и возвращает данные запрашиваемого поста
    :param login:
    :param title:
    :return:
    """
    cur.execute(f"SELECT title, description, date_of_create FROM posts WHERE title = '{title}' AND author = (SELECT user_id FROM users WHERE username = '{login}');")
    result = cur.fetchall()
    if result:
        time = result[0][2]
        return {"title": result[0][0], "description": result[0][1], "date_od_create": time.strftime("%d-%m-%y %H:%M:%S")}
    else:
        return None


def add_new_post(login, title, description):
    """
    Принимает логин, название поста и текст, и записывает все эти данные в базу данных
    :param login:
    :param title:
    :param description:
    :return:
    """
    time = datetime.datetime.now()
    cur.execute(f"INSERT INTO posts (title, description, date_of_create, author) VALUES ('{title}', '{description}', '{time}', (SELECT user_id FROM users WHERE username = '{login}'));")
    conn.commit()


def remove_post(login, title):
    """
    Удаляет пост из базы данных
    :param login:
    :param title:
    :return:
    """
    cur.execute(f"DELETE FROM posts WHERE title = '{title}' AND author = (SELECT user_id FROM users WHERE username = '{login}');")
    conn.commit()


def check_post(login, title):
    """
    Проверяет существует ли тайтл в базе данных или нет
    :param login:
    :param title:
    :return:
    """
    cur.execute(f"SELECT * from posts WHERE title = '{title}' AND author = (SELECT user_id FROM users WHERE username = '{login}');")
    result = cur.fetchall()
    if result:
        return True
    else:
        return False


def all_posts(login):
    """
    Возвращает полный список всех постов задаваемого пользователя
    :param login:
    :return:
    """
    cur.execute(f"SELECT post_id, title, description, date_of_create FROM posts WHERE author = (SELECT user_id FROM users WHERE username = '{login}')")
    result = cur.fetchall()
    if result:
        return result
    else:
        return None


if __name__ == "__main__":
    # print(login("Matvey", "Lol12345"))
    # print(check_login('Matvey'))
    # print(page_info("Matvey"))
    # print(check_pass("Matvey", "Lol12345"))
    # print(check_status("NastyaLohushka"))
    # print(get_post("Matvey", "Pirozhok"))
    add_new_post("Matvey", "Roker", "I am roker")
    # remove_post("Matvey", "Roker")