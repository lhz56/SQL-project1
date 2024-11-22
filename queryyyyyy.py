import MySQLdb as mc

conn = mc.connect(host='localhost', user='root', password='Lhzfbacc56&', database = 'menagerie')
c = conn.cursor()

c.execute("SELECT owner, COUNT(*) as num_pets FROM pet GROUP BY owner ;")
for row in c.fetchall():
    print(row)