import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Dankb2131193*'
)

current = config.cursor()


sql = '''
    SELECT * FROM phonebook ORDER BY name DESC
'''

sql2 = '''
    SELECT * FROM phonebook ORDER BY number ASC
'''

current.execute(sql2)

current.close()
config.commit()
config.close()