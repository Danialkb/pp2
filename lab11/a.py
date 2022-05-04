import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(
        host='localhost', 
        database='postgres',
        user='postgres',
        password='Dankb2131193*'
    )

    cursor = connection.cursor()
    # хранимая процедура
    cursor.callproc('filter')
    result = cursor.fetchall()
    for row in result:
        print("id = ", row[0])
        print("name = ", row[1])
        print("number = ", row[2])

except (Exception, Error) as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()