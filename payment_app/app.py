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
    
@app.route("/form", defaults={"group_name": ''})
@app.route("/form/<group_name>")
def form(group_name):
    con = sqlite3.connect(DATABASE)
    db_members = con.execute('SELECT * FROM members').fetchall()
    con.close()

    members = []
    for row in db_members:
        members.append({'id': row[0],'name': row[1]})
        
    return render_template(
        'form.html',
        members = members,
        group_name = group_name
    )

@app.route('/register_member', methods = ['POST'])
def register_member():
    
    member_name = request.form['member_name']
    
    if not member_name or not member_name.strip():
        return redirect(url_for('form'))
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO members(name) VALUES(?)',
                [member_name])
    con.commit()
    con.close()
    
    group_name = request.form['group_name']
    
    return redirect(url_for('form', group_name = group_name))
    
@app.route('/delete/<int:id>', methods = ['POST'])
def delete_member(id = None):
    
    con = sqlite3.connect(DATABASE)
    con.execute('DELETE FROM members WHERE id = ?',[id])
    con.commit()
    con.close()
    
    group_name = request.form['group_name']
    
    return redirect(url_for('form', group_name = group_name))

@app.route('/register_group', methods = ['POST'])
def register_group():
    group_name = request.form['group_name']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO groups VALUES(?)',
                [group_name])
    con.commit()
    con.close()
    
    return redirect(url_for('index'))


