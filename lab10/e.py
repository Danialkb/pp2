import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Dankb2131193*'
)

current = config.cursor()


sql = '''
    DELETE FROM phonebook WHERE name = %s
'''


current.execute(sql, ('Mom',))


current.close()

config.commit()
config.close()