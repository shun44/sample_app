from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'

db = SQLAlchemy(app)
class Task(db.Model):

    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text())
    status = db.Column(db.Integer)

db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks = tasks)

app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)
