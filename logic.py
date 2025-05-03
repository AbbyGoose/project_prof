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
    
    def results(self, user_id, user_name):
        conn = sqlite3.connect(self.database)
        with conn:
            m = 0
            cur = conn.cursor()
            cur.execute("SELECT human FROM results WHERE user_id = ? AND user_name = ?", (user_id, user_name,))
            hum = int(cur.fetchone()[0])
            cur.execute("SELECT sign FROM results WHERE user_id = ? AND user_name = ?", (user_id, user_name,))
            sig = int(cur.fetchone()[0])
            cur.execute("SELECT tech FROM results WHERE user_id = ? AND user_name = ?", (user_id, user_name,))
            tec = int(cur.fetchone()[0])
            cur.execute("SELECT nature FROM results WHERE user_id = ? AND user_name = ?", (user_id, user_name,))
            nat = int(cur.fetchone()[0])
            cur.execute("SELECT paint FROM results WHERE user_id = ? AND user_name = ?", (user_id, user_name,))
            pai = int(cur.fetchone()[0])
            if hum > m:
                m = hum
                res = 'h'
            if sig > m:
                m = sig
                res = 's'
            if tec > m:
                m = tec
                res = 't'
            if nat > m:
                m = sig
                res = 'n'
            if pai > m:
                m = sig
                res = 'p'
                return res
        
    def delete_use(self, user_id, user_name):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('UPDATE results SET human = 0, sign = 0, tech = 0, nature = 0, paint = 0 WHERE user_id = ? AND user_name = ?', (user_id, user_name,))
            

que = {'Разрабатывать компьютерные программы и алгоритмы': 'sign', 'Вести занятия в фитнес-зале': 'human', 'Обрабатывать фотографии с помощью компьютерных программ': '', 'Управлять каким-либо видом техники (автомобиль, самолет, мотоцикл)': 'tech', 
       'Ухаживать за домашними животными': 'nature', 'Обрабатывать музыкальные композиции': '', 'Анализировать изменения цен акций на бирже': 'sign', 'Исследовать поведение животных в искусственных лабораторных условиях': 'nature', 
       'Лечить людей или помогать им психологически': 'human', 'Ремонтировать и настраивать компьютерную технику': 'tech', 'Проводить предпродажное тестирование смартфонов и компьютерной техники': 'tech', 'Заниматься обработкой и анализом собранных данных': 'sign', 
       'Вести свой блог или писать статьи для различных изданий': '', 'Анализировать и определять самые выгодные способы доставки товаров': 'sign', 'Проверять исправность систем самолета перед вылетом': 'tech', 'Заниматься оформлением выставок и витрин': '', 
       'Заниматься разведением и дрессировкой породистых собак': 'nature', 'Заниматься сборкой и настройкой интернет оборудования и компьютеров': 'tech', 'Находить неисправности в автомобилях, ремонтировать их': 'tech', 'Изучать микроорганизмы и бактерии': 'nature', 
       'Проверять правильность заполнения документов': 'sign', 'Проверять правильность работы офисного оборудования': 'tech', 'Заниматься поиском месторождений полезных ископаемых': 'nature', 'Изобретать новые бытовые электроприборы': 'tech', 
       'Контролировать работу промышленного оборудования': 'tech', 'Обрабатывать собранные данные страховой компании': 'sign', 'Обучать учеников или студентов': 'human', 'Систематизировать книги в библиотеке': 'sign', 
       'Создавать новые модели одежды или аксессуаров': '', 'Вести документооборот в компании': 'sign', 'Подбирать для туристов оптимальные места отдыха': 'human', 'Придумывать сценарии и декорации для праздников': '', 
       'Следить за состоянием лесов': 'nature', 'Создавать дизайн сайтов, иллюстрации в журналах': '', 'Участвовать в театральных постановках': '', 'Разводить редких, экзотических животных': 'nature', 
       'Составлять сценарии для промороликов и флешмобов': '', 'Обеспечивать безопасность корпоративной сети': 'sign', 'Редактировать тексты, находя и исправляя в них ошибки': 'sign', 'Консультировать и помогать людям с помощью телефона': 'human', 
       'Переводить фильмы и сериалы на другие языки': 'sign', 'Заниматься реставрацией исторических артефактов': '', 'Следить за курсами валют и акций, участвовать в торгах': 'sign', 'Участвовать в геологических экспедициях': 'nature', 
       'Проводить генетические исследования': 'nature', 'Следить за правопорядком в общественных местах': 'human', 'Во время поездок и перелетов сопровождать и помогать пассажирам': 'human', 'Создавать новое оборудование для промышленности': 'tech', 
       'Анализировать экологическое состояние природы': 'nature', 'Руководить туристической группой в походе': 'human', 'Проводить оптимизацию работы сайта': 'sign', 'Находить и изучать строение новых видов животных': 'nature', 
       'Участвовать в пресс-конференциях': 'human', 'Заниматься ландшафтным дизайном, архитектурой зданий': '', 'Общаться с соискателями на должность': 'human', 'Спасать и защищать исчезающие виды животных': 'nature', 
       'Заниматься прокладкой и монтажом оптоволоконных линий': 'tech', 'Продавать редкие товары, убеждая клиента купить': 'human', 'Заниматься воспитанием детей': 'human', 'Создавать дизайн персонажей компьютерных игр': '', 
       'Проводить тренинги и семинары': 'human', 'Изучать поведение морских животных': 'nature', 'Заниматься разметкой данных и обучением нейронных сетей': 'sign', 'Заниматься написанием своей книги': '', 
       'Управлять армейским дроном для разведки': 'tech', 'Проверять организации на правильность ведения документации': 'sign', 'Координировать деятельность работников магазина': 'human', 'Быть солистом музыкальной группы': '', 
       'Заниматься генной модификацией': 'nature', 'Проектировать роботов и роботизированные системы': 'tech', 'Руководить детской спортивной секцией': 'human', 'Создавать приложения для смартфонов': 'sign', 
       'Наблюдать за изменениями погоды, строить прогнозы': 'nature', 'Делать необычные декоративные предметы': '', 'Консультировать клиентов о производимой продукции': 'human', 'Проводить технологическую проверку качества': 'tech', 
       'Настраивать оборудование для татуирования': 'tech', 'Рисовать эскизы татуировок': '', 'Разрабатывать новые лекарственные средства': 'nature', 'Вести строгий учет движения денежных средств': 'sign', }

if __name__ == '__main__':
    manager = DatabaseManager(database)
    manager.create_tables()