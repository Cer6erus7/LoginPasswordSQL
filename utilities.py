import psycopg2


conn = psycopg2.connect(dbname="loginpasswordsql", user="cer6erus7")

def login(login, password):
    """
    Принимает логин и пароль пользователя. Делает запрос в базу данных postgreSQL и запрашивает данные введенные
    пользователем, если же эти данные существуют и совпадают с пользовательскими, функция возвращает истинну, если
    же не совпадают, ложь
    :param login:
    :param password:
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT username, password FROM users WHERE username = '{login}'")
    result = cur.fetchall()
    try:
        if result[0][0] == login and result[0][1] == password:
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    print(login("Matvey", "Lol12345"))