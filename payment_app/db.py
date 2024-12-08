import sqlite3

DATABASE = 'database.db'


def create_members_table():
    #DATABASEはデータベース名
    con = sqlite3.connect(DATABASE)
    #bookはテーブル名
    con.execute("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL)")
    con.close

def create_group_table():
    #DATABASEはデータベース名
    con = sqlite3.connect(DATABASE)
    #bookはテーブル名
    con.execute("CREATE TABLE IF NOT EXISTS groups (name)")
    con.close
    
def delete_table():
    con = sqlite3.connect(DATABASE)
    con.execute("DROP TABLE members")
    con.execute("DROP TABLE groups")
    
    con.close
    
    