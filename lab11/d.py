import psycopg2 
from psycopg2 import Error 
 
try: 
    connection = psycopg2.connect( 
        host='localhost',  
        database='postgres', 
        user='postgres', 
        password='Dankb2131193*' 
    ) 
 
    cursor = connection.cursor() 
    # хранимая процедура 
    cursor.callproc('pagination') 
    result = cursor.fetchall() 
    for i in result: 
        print(*i) 
 
except (Exception, Error) as error: 
    print("Ошибка", error) 
finally: 
    if connection: 
        cursor.close() 
        connection.close()