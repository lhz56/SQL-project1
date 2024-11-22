import MySQLdb as mc

conn = mc.connect(host='localhost', user='root', password='Lhzfbacc56&', database = 'menagerie')
c = conn.cursor()

c.execute("SELECT * FROM pet;")
for row in c.fetchall():
    print(row)