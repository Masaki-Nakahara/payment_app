import sqlite3

DATABASE = 'database.db'


con = sqlite3.connect(DATABASE)
print(con.execute("SELECT * FROM members").fetchall())

con.close


