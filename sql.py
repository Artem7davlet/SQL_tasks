import sqlite3

def limit_task1(cursor):
     cursor.execute('select * from workers limit 6')
     print(cursor.fetchall())

def limit_task2(cursor):
     cursor.execute('select * from workers limit 3 offset 1')
     print(cursor.fetchall())

def order_by_task1(cursor):
     cursor.execute("select * from workers order by salary asc")
     print(cursor.fetchall())

def order_by_task2(cursor):
     cursor.execute('select * from workers order by salary desc')
     print(cursor.fetchall())

def order_by_task3(cursor):
     cursor.execute('select * from (select * from workers limit 5 offset 1) order by age')
     print(cursor.fetchall())

def count_task1(cursor):
     cursor.execute("select count(*) from workers")
     print(cursor.fetchall())

def like(cursor):
     cursor.execute("select * from pages")
     print(cursor.fetchall())

def like_task1(cursor):
     cursor.execute("SELECT * FROM pages WHERE author LIKE '%ов %' ")
     print(cursor.fetchall())

def like_task2(cursor):
     cursor.execute("SELECT * FROM pages WHERE article LIKE '% элемент%' ")
     print(cursor.fetchall())

def like_task3(cursor):
     cursor.execute("SELECT * FROM workers WHERE age LIKE '3_' ")
     print(cursor.fetchall())

def like_task4(cursor):
     cursor.execute("SELECT * FROM workers WHERE name LIKE '%a' ")
     print(cursor.fetchall())


w = [("Ладюша", 18, 400),
     ("Дилярушка", 17, 500),
     ("Лейладжон", 14, 500),
     ("Аделинаджон", 16, 1000),
     ("Элинушка", 19, 500),
     ("Анюша", 15, 1000),
     ("Эльзахон", 17, 2000),
     ("Амалишка", 18, 1700),
     ("Сонюша", 16, 2540),
     ("Каринушка", 16, 1890),
     ("Луизахон", 18, 2570),
     ("Настюша (Шеф)", 14, 1698),
     ("Иделиябону", 19, 2578)]
con = sqlite3.connect("firstDB1.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    salary INTEGER
                )''')
cursor.executemany('INSERT INTO workers (name, age, salary) VALUES (?, ?, ?)', w)

t = [("Архипов Артем",	"В своей статье рассказывает о машинах."),
     ("Бабаджанов Камолджон",	"Написал статью об инфляции."),
     ("Веткин Даниил",	"Придумал новый химический элемент."),
     ("Коснырев Лев",	"Также писал о машинах."),
     ("Низамов Ильнар",	"Написал статью о том, как разрабатывать элементы дизайна."),
     ("Мубаракшин Булат",	"Написал статью о своей девушке."),
     ("Трифонов Илья",	"Также писал о девушке")]

cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author TEXT,
                    article TEXT
                )''')
con.commit()
cursor.executemany('INSERT INTO pages (author, article) VALUES (?, ?)', t)

like_task3(cursor)