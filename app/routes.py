from app import app 
from flask import render_template
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/memberhome')
def memberhome():
    return render_template('memberhome.html')