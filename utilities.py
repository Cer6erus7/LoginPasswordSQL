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
    cur.execute(f"SELECT username, password FROM users WHERE username = '{login}'")
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


if __name__ == "__main__":
    print(login("Matvey", "Lol12345"))
    print(check_login('Matvey'))