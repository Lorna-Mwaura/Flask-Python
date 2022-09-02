from flask import Flask, render_template
from . import main


@main.route('/')
def sign_up():
    return render_template('user/signup.html')

@main.route('/login')
def login():
    return render_template('user/login.html')


@main.route('/home')
def index():
    return render_template('index.html')

