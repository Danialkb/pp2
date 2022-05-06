import psycopg2 
from psycopg2 import Error 
 
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
            print('Function is created') 
 
 
postgresql_func = """ 
CREATE OR REPLACE FUNCTION pagination() 
    RETURNS TABLE(id integer, name varchar, number varchar)  
    AS $$ 
BEGIN 
    RETURN QUERY 
    SELECT * FROM phonebook LIMIT 5 OFFSET 3; 
END; 
$$  
LANGUAGE plpgsql; 
""" 
create_func(postgresql_func)