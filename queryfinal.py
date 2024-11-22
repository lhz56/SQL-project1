import MySQLdb as mc

conn = mc.connect(host='localhost', user='root', password='Lhzfbacc56&', database = 'menagerie')
c = conn.cursor()

c.execute(""" SELECT name, birth, MONTH(birth) FROM pet; """)
conn.commit()

rows = c.fetchall()

print(f"{'name':<10}{'birth':<15}{'MONTH(birth)'}")
for row in rows:
    birth_date = row[1].strftime('%Y-%m-%d') if row[1] else "NULL"
    print(f"{row[0]:<10}{birth_date:<15}{row[2]}")

c.close()
conn.close()