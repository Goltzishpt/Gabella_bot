import sqlite3


class BotDB:

    def __init__(self, db_file):
        '''Инициалиация соединения с БД'''
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        '''Проверяем, есть ли юзер в БД'''
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?", (user_id,))
        print(result, 'result')
        return bool(result)

    def insert_date(self, user_id, user_age, user_sex, user_choice, user_city, user_name,user_info, user_blob):
        '''Добавление юзера в БД'''
        self.cursor.execute(f"INSERT INTO users(user_id, user_age, user_sex, user_choice, user_city, user_name, \
        user_info, user_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?", (user_id, user_age, user_sex, user_choice, user_city, user_name, \
        user_info, user_blob, ))


    def close(self):
        self.conn.close()
