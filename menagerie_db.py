import MySQLdb as mc

conn = mc.connect(host='localhost', user='root', password='Lhzfbacc56&')
c = conn.cursor()

c.execute('SHOW DATABASES;')
databases = c.fetchall()
for db in databases:
    print(db)

c.execute(""" DROP DATABASE IF EXISTS menagerie; """)
