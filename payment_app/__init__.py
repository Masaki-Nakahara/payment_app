from flask import Flask

app = Flask(__name__)

from payment_app.app import *

from payment_app import db
#空のテーブルの取得
db.create_members_table()
db.create_group_table()