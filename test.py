import sqlite3

con = sqlite3.connect('store.db')
cur = con.cursor()
cur.execute("select * from product")
print(cur.fetchone())
