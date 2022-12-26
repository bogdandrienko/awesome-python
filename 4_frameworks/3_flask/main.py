from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import requests
from bs4 import BeautifulSoup
import psycopg2
import random

# Model View Controller

# 127.0.0.1:5432 (localhost:5432) - текущая машина, откуда идёт запрос
# 192.168.1.121:5432 - локальный адрес текущей машины в этой подсети
# 89.218.132.130:80 - внешний "белый" ip-адрес от Казактелекома
# km.kz - домен первого уровня
# web.km.kz (89.218.132.130) - домен второго уровня

app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


@app.route("/hello/", methods=['GET'])
def hello():
    return "<h1>Hello World</h1>"


@app.route("/", methods=['GET'])  # 'http://127.0.0.1:8000' + '/' - маршрут в браузерной строке
def home():
    name = "Python"
    return render_template('home.html', name=name)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        with open('temp/db.json', 'r') as file:
            json_obj = json.load(file)
        return render_template('login.html', username=json_obj["username"], password=json_obj["password"])
    elif request.method == "POST":
        # послать с фронтенда данные (заполненную форму для регистрации пользователя)
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"email: {email}")
        print(f"email: {password}")

        with open('temp/db.json', 'w') as file:
            print('\n\n\n\n\n!!!!!!!!!!\n\n\n\n')
            json.dump({"username": email, "password": password}, file)
        return render_template('login.html', status=200)
    else:
        return "<h1>METHOD NOT ALLOWED</h1>"


def parse_data():
    url = 'https://kolesa.kz/mototehnika/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/77.0.3865.90 Safari/537.36"}

    response = requests.get(url=url, headers=headers)
    data1 = response.text
    bs4obj = BeautifulSoup(data1, 'html.parser')
    objects = bs4obj.find_all('div', class_="a-list__item")  # вся техника!

    lists = ""
    for obj in objects:
        try:
            price = int(
                ''.join(str(obj.find('span', class_="a-card__price")).split('>')[1].split('<')[0].strip().split())
            )
            model = str(obj.find('h5', class_="a-card__title")).split('</a>')[0].split('target="_blank">')[1].strip()
            print(f"{model}: {price}")
            print('\n\n\n*********************************************************\n\n\n')
            lists += f"<li><strong>{model}</strong>: {price}</li>"
        except Exception as error:
            print(error)
    return f"<ul>{lists}</ul>"

# -- CRUD create read update delete:
#
# -- SELECT * FROM public.zarplata ORDER BY id ASC -- Выборка с сортировкой
# -- SELECT * FROM public.zarplata where alive = '0' -- Условная выборка
# -- SELECT name, value FROM public.zarplata ORDER BY id ASC -- Выборка определённых полей
# -- SELECT * FROM public.zarplata ORDER BY value desc, id desc -- desc | acs
# -- SELECT sum(value) FROM public.zarplata -- sum, max, min, avg,
# -- SELECT min(value), position FROM public.zarplata GROUP by position
#
# -- INSERT INTO public.zarplata (id, name, position, value, alive) VALUES
# ('8', 'Alice', 'programmer', '210000', '0') -- Вставка строки
#
# -- INSERT INTO public.zarplata (id, name, position, value, alive) VALUES
# ('11', 'Alice', 'programmer', '111', '1'), ('10', 'Alice', 'programmer', '222', '1') -- Вставка строк
#
# -- UPDATE public.zarplata SET value = value + 666 where alive = '1'
#
# -- DELETE FROM public.zarplata where name = 'Тлеген2'
#
# -- SELECT * FROM public.zarplata

def start(name):
    # Server = host = ip = localhost = 127.0.0.1
    # connection_string = 'DRIVER={PostgreSQL Unicode};' \
    #                     'Server=127.0.0.1;' \
    #                     'Port=5432;' \
    #                     'Database=zarplata;' \
    #                     'User ID=postgres;' \
    #                     'Password=31284bogdan;' \
    #                     'String Types=Unicode'

    connection_string = "dbname=zarplata user=postgres password=31284bogdan"

    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False

    try:
        # while True:
        #     username = input("Введите своё имя")
        #     if len(username) > 3:
        #         break

        # anything
        # sql_string = "SELECT * FROM public.zarplata"
        # sql_string = "SELECT * FROM public.zarplata where alive = '0'"
        # sql_string = f"INSERT INTO public.zarplata VALUES ('7', '{str(username)}', 'programmer', '6666', '0')"

        # class User:
        #     def __init__(self, id, name):
        #         self.id = id
        #         self.name = name
        # users = [User(id=x, name=f"Alice{x}") for x in range(200, 300)]

        sql_string = "INSERT INTO public.zarplata (id, name, position, value, alive) VALUES "
        for x in range(101, 200):
            sql_string += f" ('{x}', 'Alice{x}', 'programmer', " \
                          f"'{random.randint(20000, 60000) * x}', '{random.randint(0, 1)}'), "

        # datas = [
        #     {
        #         "id": x,
        #         "name": f"Alice{x}",
        #         "position": "programmer",
        #         "value": random.randint(20000, 60000) * x,
        #         "alive": random.randint(0, 1)
        #     } for x in range(20, 100)
        # ]
        # for row in datas:
        #     sql_string += f""" ('{row["id"]}', '{row["name"]}', '{row["position"]}',
        #                 '{row["value"]}', '{row["alive"]}'), """
        # print(f"datas: {datas}")
        sql_string = sql_string[:-2:]

        # sql_string = "INSERT INTO public.zarplata (id, name, position, value, alive) VALUES " \
        #              "('11', 'Alice', 'programmer', '111', '1'),  " \
        #              "('10', 'Alice', 'programmer', '222', '1')"
        #
        cursor.execute(sql_string)
        try:
            # data = cursor.fetchone()
            data = cursor.fetchall()  # [(5, 'Alice', 'programmer', 210000, False), (1, 'Bogdan', 'programmer', 200...]
            print(f"data: {data}")
        except Exception as error:
            print(error)
    except Exception as error:
        print(error)
        connection.rollback()
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()


# Страница с добавлением задачи                (POST) Create / Insert
# Страница с просмотром всех задач             (GET) Get all / Select
# Страница с просмотром детально одной задачи  (GET) Get one / Select
# Функция для удаления задачи                  (DELETE) DELETE one / DELETE
# Страничка с обновлением уже существующей     (PUT) UPDATE / UPDATE

def db():
    # connection_string = "dbname='flask_database' user='postgres' host='localhost' password='31284bogdan'"
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute("""INSERT INTO zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');""")
        cursor.execute("""select * from zarplata;""")
        # print(10 - "")  #
        # print({"name": "Bogdan"}["username"])  #
        data = cursor.fetchall()
        print(data)
        print(len(data))
        print(10 / 0)  # ZEROdivision
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()


@app.route("/todo_create", methods=['GET', 'POST'])
def todo_create():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status', False)

        print(f"title: {title}")
        print(f"description: {description}")
        print(f"status: {status}")

        conn = psycopg2.connect("dbname=flask_db user=postgres password=31284bogdan")
        cur = conn.cursor()

        query_string = f"""
        INSERT INTO public.flask_table (title, description, status) 
        VALUES ('{title}', '{description}', '{status}')
        """
        cur.execute(query_string)
        conn.commit()
        cur.close()
        conn.close()

    return flask.render_template('todo_create.html')


@app.route("/todo_create/", methods=['POST'])
def todo_create():
    username = request.form.get('username')
    salary = request.form.get('salary')

    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute(f"""INSERT INTO zarplata (username, salary) VALUES ('{str(username)}', '{int(salary)}');""")
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return redirect(url_for('todo_list'))


@app.route("/todo_list")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def todo_list():
    conn = psycopg2.connect("dbname=flask_db user=postgres password=31284bogdan")
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM public.flask_table
    ORDER BY id ASC
    """)
    records = cur.fetchall()
    cur.close()
    conn.close()
    task_list = [{"title": x[0], "description": x[1][:5], "status": x[2], "id": x[3]} for x in records]

    print(task_list)
    print(type(task_list))

    context = {
        "task_list": task_list,
        "username": "Роман"
    }
    return render_template('todo_list.html', **context)


@app.route("/todo_list/", methods=['GET'])
def todo_list():
    todos = []
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute("""select * from zarplata;""")
        # print(10 - "")  #
        # print({"name": "Bogdan"}["username"])  #
        data = cursor.fetchall()
        print(data)
        todos = data
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    todos_temp = []
    if len(todos) > 0:
        for i in todos:
            todos_temp.append({"id": i[0], "name": i[1], "salary": i[2]})
    todos = todos_temp

    # todos = [{"id": x, "name": f"Clear cat #{x}", "salary": 60000 + x * 100} for x in range(1, 30+1)]
    return render_template('Todo_list.html', todos=todos)  # **kwargs


@app.route("/todo/<todo_id>")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def todo_by_id(todo_id):
    conn = psycopg2.connect("dbname=flask_db user=postgres password=31284bogdan")
    cur = conn.cursor()

    cur.execute(f"""
        SELECT * FROM public.flask_table
        WHERE id = '{todo_id}'
        """)
    record = cur.fetchall()[0]
    cur.close()
    conn.close()
    print(record)
    record = {
        "title": record[0], "description": record[1],
        "status": record[2], "id": record[3]
    }
    return render_template('todo_detail.html', task=record)


@app.route("/todo_detail/<todo_id>/", methods=['GET'])
def todo_detail(todo_id):
    todo = {}
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute(f"""select * from zarplata where id = '{todo_id}';""")
        # print(10 - "")  #
        # print({"name": "Bogdan"}["username"])  #
        data = cursor.fetchone()
        print(data)
        todo = data
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    if todo is not None:
        todo = {"id": todo[0], "name": todo[1], "salary": todo[2]}
    else:
        todo = {}

    return render_template('Todo_detail.html', todo=todo)  # **kwargs


@app.route("/get_all_rows/")
def get_all_rows():
    conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
    cur = conn.cursor()
    query_string = """
    SELECT * FROM public.example_table
    ORDER BY id ASC
    """
    cur.execute(query_string)
    records = cur.fetchall()
    cur.close()
    conn.close()
    data = jsonify(records)
    return data
