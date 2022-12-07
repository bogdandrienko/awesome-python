import psycopg2

try:
    # number = input("Введите номер id: ")

    class RowObj:
        def __init__(self, row: tuple):
            self.username = row[0]
            self.age = row[1]
            self.married = row[2]
            self.credits = row[3]
            self.id = row[4]

    arr = [
        ('x', 12, 'false', 888.888, 85),
        ('y', 13, 'false', 888.888, 86),
        ('z', 14, 'false', 888.888, 87),
        ('a', 15, 'false', 888.888, 88),
        ('b', 16, 'false', 888.888, 89),
    ]
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    connection.autocommit = True
    cursor = connection.cursor()
    for row in arr:
        obj = RowObj(row=row)
        query_string = f'''INSERT INTO public.example_table 
        (username, age, married, credits, id) values 
        ('{obj.username}', {obj.age}, {obj.married}, {obj.credits}, {obj.id})'''
        cursor.execute(query_string)
        # connection.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
    
    
###############################################################################################

import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    connection.autocommit = True
    cursor = connection.cursor()
    query_string = '''
UPDATE public.example_table
SET credits = '0.0'
WHERE married = 'true'
    '''
#     query_string = '''
# CREATE TABLE public.table1
# (
#     title text NOT NULL,
#     id serial NOT NULL,
#     PRIMARY KEY (id)
# );
#
# ALTER TABLE IF EXISTS public.table1
#     OWNER to postgres;
#     '''
    cursor.execute(query_string)
    # connection.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
    
##################################################################################################

import psycopg2
from api import utils

try:
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    cursor = connection.cursor()
    query_string = '''
SELECT * FROM public.example_table
WHERE age = 50
ORDER BY id ASC
    '''
    cursor.execute(query_string)
    records = cursor.fetchall()
    print(records)
    print(type(records))
    for i in records:
        print(i)
        print(type(i))
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()




# obj = utils.SQL(
#     autocommit=True,
#     user="postgres",
#     password="31284bogdan",
#     host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
#     port="5432",
#     dbname="example",
# )
# records = obj.execute('''
# SELECT * FROM public.example_table
# WHERE age = 50
# ORDER BY id ASC
#     ''')
# print(records)
#
#
# records = obj.execute('''
# SELECT * FROM public.example_table
# WHERE id > 50
# ORDER BY id ASC
#     ''')
# print(records)

################################################################################################

import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    cursor = connection.cursor()
    query_string = '''
DELETE FROM public.example_table
WHERE id = 888
    '''
    cursor.execute(query_string)
    connection.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
    
###############################################################################################


