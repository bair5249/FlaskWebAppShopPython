from psycopg2 import connect


'''
Обозначения 
Логи - *****LOG*****
Ошибки - *****ERROR*****
'''


class ConnectToDatabase:  # Здесь мы подключаемся к базе данных
    def __init__(self, host, db_port, dbname, db_user, db_password):  # Все данные приходят к нам из main.py
        self.log = "*****LOG*****"
        self.err = "*****ERROR*****"
        try:  # А main.py получает их из файла cfg_file.py
            self.con = connect(dbname=dbname,
                               host=host,
                               port=db_port,
                               user=db_user,
                               password=db_password)
            self.con.autocommit = True  # Для того, чтобы таблица обновлялась после каждого запроса
            self.cursor = self.con.cursor()
        except Exception as e:
            self.close_db()
            print(self.err, " Ошибка подключения: ", e, self.err)

    def close_db(self):
        self.cursor.close()
        self.cursor.close()
        print(self.log, " Соединение закрыто ", self.log)

    def show_admins(self):
        try:
            self.cursor.execute("SELECT * FROM site_admins")
            data = self.cursor.fetchall()
            lst = []
            for row in data:
                print(row)
                row_data = {
                    "id": row[5],
                    "username": row[0],
                    "password": row[1],
                    "lastname": row[2],
                    "firstname": row[3],
                    "date_of_birth": row[4]
                }
                lst.append(row_data)
            print(self.log, " Успешный вывод админов ", self.log)
            return lst
        except Exception as e:
            print(self.err, " Ошибка вывода админов: ", e, self.err)

    def adding_admin(self, admin_data):
        try:
            self.cursor.execute(f"INSERT INTO public.site_admins"
                                f"(bairs_username, bairs_password, lastname, firstname, date_of_birth) "
                                f"VALUES "
                                f"('{admin_data.username}', "
                                f"'{admin_data.password}', "
                                f"'{admin_data.lastname}', "
                                f"'{admin_data.firstname}', "
                                f"'{admin_data.date_of_birth}');")
            print(self.log, " Успешное добавление админа \n", "Данные добавленного админа: ",
                  admin_data
                  , self.log)
        except Exception as e:
            print(self.err, " Ошибка добавления админа: ", e, "\nДанные, которые не удалось вставить: ",
                  admin_data, self.err)
