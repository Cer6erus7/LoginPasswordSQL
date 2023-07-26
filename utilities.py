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


def check_status(login):
    """
    Проверяет данные о статусе профиля
    :param login:
    :return:
    """
    cur.execute(f"SELECT status FROM users WHERE username = '{login}'")
    result = cur.fetchall()
    if result[0][0] == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    # print(login("Matvey", "Lol12345"))
    # print(check_login('Matvey'))
    # print(page_info("Matvey"))
    print(check_pass("Matvey", "Lol12345"))
    print(check_status("NastyaLohushka"))