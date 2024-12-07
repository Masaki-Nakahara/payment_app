import sqlite3

DATABASE = 'database.db'


def create_books_table():
    #DATABASEはデータベース名
    con = sqlite3.connect(DATABASE)
    #bookはテーブル名
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price)")
    con.close