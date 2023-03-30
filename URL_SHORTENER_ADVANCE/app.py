from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners
from datetime import datetime
import random
import string
import os 

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tushar'

db = SQLAlchemy(app)
Migrate(app,db)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    def __init__(self, username, password):
        self.username = username
        self.pssword = password

def generate_short_url():
    length = 6
    while True:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        url = Url.query.filter_by(short_url=short_url).first()
        if not url:
            return short_url

@app.route('/')
def home():
    if 'username' in session:
        return redirect('/dashboard')
    else:
        return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=password)
        if user:
            flash('Username aldready exists!')
            return redirect(url_for('signup'))
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
        return redirect('/login')
    else :
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=password)
        if user is not None:
            session['username'] = username
            return redirect('/shortener')
        else:
            return render_template('index.html',error='Invalid username or password!')
    else :
        return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.route('/shortener', methods=['GET', 'POST'])
def shortener():
    if request.method == 'POST':
        original_url = request.form.get('url')
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(original_url)
        # short_url = generate_short_url()
        url = Url(original_url=original_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()
        return render_template('dashboard.html',short_url=short_url)
    return render_template('dashboard.html')
    
    
@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = Url.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

@app.route('/urls')
def urls():
    urls = Url.query.all()
    return render_template('urls.html',urls=urls)

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)