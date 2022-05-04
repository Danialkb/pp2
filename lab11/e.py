import psycopg2
from psycopg2 import Error
n_name = input()
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(
        host='localhost', 
        database='postgres',
        user='postgres',
        password='Dankb2131193*'
    )

    cursor = connection.cursor()
    cursor.execute('CALL deleteuser(%s)', (n_name,))
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()