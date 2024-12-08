import sqlite3

DATABASE = 'database.db'


con = sqlite3.connect(DATABASE)
con.execute("DROP TABLE members")
con.execute("DROP TABLE groups")
con.close


