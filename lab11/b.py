import psycopg2
from psycopg2 import Error
n_id, n_name, n_number = int(input()), input(), input()
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(
        host='localhost', 
        database='postgres',
        user='postgres',
        password='Dankb2131193*'
    )

    cursor = connection.cursor()
    cursor.execute('CALL adduser(%s, %s, %s)', (n_id, n_name, n_number))
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()