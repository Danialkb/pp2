import psycopg2
from psycopg2 import Error

# n_id, n_name, n_number = int(input()), input(), input()

def create_func(query):
    try:
        connection = psycopg2.connect(
            host='localhost', 
            database='postgres',
            user='postgres',
            password='Dankb2131193*'
            )
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Procedure is created')

postgresql_proc = """
CREATE OR REPLACE PROCEDURE deleteuser(n_name varchar) AS $$ 
BEGIN
    DELETE FROM phonebook WHERE name = n_name;
END;
$$ LANGUAGE plpgsql
"""
create_func(postgresql_proc)