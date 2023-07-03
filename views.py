from flask import Blueprint, render_template, request, redirect
from suck_it import suck_it

views = Blueprint(__name__, 'views')

@views.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(f'{user}')
    else:    
        return render_template('index.html')

@views.route('/<string:usr>')
def user(usr):
    suck_it(usr)
    return f"<img src='static/out.gif' width='100%' height='100%'>"