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
CREATE OR REPLACE PROCEDURE adduser(n_id integer, n_name varchar, n_number varchar) AS $$ 
BEGIN
    IF EXISTS (select * from phonebook where name = n_name) THEN UPDATE phonebook SET number = n_number where name = n_name;
        
    ELSE
        INSERT INTO phonebook Values (n_id, n_name, n_number);
END IF;
end 
$$ LANGUAGE plpgsql
"""
create_func(postgresql_proc)