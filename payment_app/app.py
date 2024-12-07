from payment_app import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'
   
@app.route("/")
def index():
    con = sqlite3.connect(DATABASE)
    db_members = con.execute('SELECT * FROM members').fetchall()
    con.close()

    members = []
    
    for row in db_members:
        members.append({'name': row[0]})
        
    return render_template(
        'index.html',
        members = members
    )
    
    
@app.route("/form")
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods = ['POST'])
def register():
    name = request.form['name']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO members VALUES(?)',
                [name])
    con.commit()
    con.close()
    
    return redirect(url_for('index'))
    
print('hello')