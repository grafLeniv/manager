from models import User, Task, Col

from app import app
from app import db


from flask import Flask, url_for, render_template, request, redirect, session



@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            return render_template('index.html', data=getfollowedby(username))
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        session['name'] = name
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('taskman'))
            else:
                return 'Error login/pass'
        except:
            return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.route('/test', methods=['GET', 'POST'])
def test():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('ek.html')


@app.route('/taskman', methods=['GET', 'POST'])
def taskman():
    tasks = Task.query.all()

    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('taskman.html', tasks=tasks)

@app.route('/info')
def info():
#    if not session.get('logged_in'):
#        return render_template('login.html')
#    else:
    return render_template('info.html')

@app.route('/contact')
def contact():
#    if not session.get('logged_in'):
#        return render_template('login.html')
#    else:
    return render_template('contact.html')

#Обработчик статуса ошибки
@app.errorhandler(404)
def exception_handler(e):
    return render_template('info.html'), 404