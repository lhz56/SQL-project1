import MySQLdb as mc

conn = mc.connect(host='localhost', user='root', password='Lhzfbacc56&', database = 'menagerie')
c = conn.cursor()

c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
for row in c.fetchall():
    print(row)