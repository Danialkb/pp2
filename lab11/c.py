import psycopg2
from psycopg2 import Error
import re
mylist = [
    (54, 'dan', '87759654547'),
    (6, 'karen', '87774754547'),
    (8, 'naga', '87788885651'),
    (14, 'popl', '87762275377'),
    (14, 'pop', '87072275377')
    
]
incorrect = []
pattern = r'^8777[0-9]{7}$|^8747[0-9]{7}$|^8778[0-9]{7}$|^8700[0-9]{7}$|^8707[0-9]{7}$|^8708[0-9]{7}$|^8705[0-9]{7}$|^8775[0-9]{7}$' 
for i in mylist:
    if re.search(pattern, i[2]) == None:
        mylist.remove(i)
        incorrect.append(i)
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(
        host='localhost', 
        database='postgres',
        user='postgres',
        password='Dankb2131193*'
    )

    cursor = connection.cursor()
    cursor.executemany('CALL adduser(%s, %s, %s)', mylist)
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()
print(f'List of incorrect values: {incorrect}')