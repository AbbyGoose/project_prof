import sqlite3
from config import *
class DatabaseManager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS results (
                user_id INTEGER,
                user_name TEXT,
                human TEXT,
                sign TEXT,
                tech TEXT,
                nature TEXT,
                paint TEXT
            )
        ''')

            conn.commit()

    def add_user(self, user_id, user_name):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM results")
            exist = cur.fetchone()
            if exist is None:
                cur.execute('''INSERT INTO results (user_id, user_name, human, sign, tech, nature, paint) VALUES (?, ?, 0, 0, 0, 0, 0)''', (user_id, user_name))
                conn.commit()
            else:
                pass
            return 1

  
    def add_res(self, user_id, user_name, res):
        conn = sqlite3.connect(self.database)
        with conn:
            if res == 'human':
                conn.execute('''UPDATE results SET human = human+1 WHERE user_id = ? AND user_name = ?''', (user_id, user_name,))
                conn.commit()
            elif res == 'sign':
                conn.execute('''UPDATE results SET sign = sign+1 WHERE user_id = ? AND user_name = ?''', (user_id, user_name,))
                conn.commit()
            elif res == 'tech':
                conn.execute('''UPDATE results SET tech = tech+1 WHERE user_id = ? AND user_name = ?''', (user_id, user_name,))
                conn.commit()
            elif res == 'nature':
                conn.execute('''UPDATE results SET nature = nature+1 WHERE user_id = ? AND user_name = ?''', (user_id, user_name,))
                conn.commit()
            else:
                conn.execute('''UPDATE results SET paint = paint+1 WHERE user_id = ? AND user_name = ?''', (user_id, user_name,))
                conn.commit()
            return 1
          
que = {'Разрабатывать компьютерные программы и алгоритмы': 'sign', 'Вести занятия в фитнес-зале': 'human', '': '', '': '', '': '',}

if __name__ == '__main__':
    manager = DatabaseManager(database)
    manager.create_tables()