from flaskr import app
from flask import render_template, request, redirect, url_for
# from flask_httpauth import HTTPBasicAuth
import sqlite3



DATABASE = 'database.db'

# auth = HTTPBasicAuth()

# users = {
#     "test_user": "test_password"
# }

# @auth.get_password
# def get_pw(username):
#     if username in users:
#         return users.get(username)
#     return None
    

@app.route("/")
def index():
    con = sqlite3.connect(DATABASE)
    #.hetchall()→全てのデータを、pythonのリストオブジェクトで取得
    #データベースの1行が1つのタプルになっていて、それが要素になっているリストを返す
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()
    
    books = []
    for row in db_books:
        books.append({'title': row[0], 'price': row[1]})
        
    # books = [{
    #     "title" : "ぐりとぐら",
    #     "price" : "300"
    # },{
    #     "title" : "バムとケロ",
    #     "price" : "500"
    # }]
    return render_template(
        'index.html',
        books = books
    )
@app.route("/form")
def form():
    return render_template(
        'form.html'
    )

# @auth.login_required
# def hello():
#     return "Hello World!"

@app.route('/register', methods = ['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?,?)',
                [title, price])
    con.commit()
    con.close()
    
    return redirect(url_for('index'))
    
    
    
print('Hello!')
print('happy!')