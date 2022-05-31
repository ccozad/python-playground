from flask import Flask, request, Response
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.app = app

from routes import level, enemy, enemy_instance


db.init_app(app)
