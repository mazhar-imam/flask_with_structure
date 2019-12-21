from flask import render_template, url_for, flash, redirect
from my_app import app
from my_app.forms import RegistrationForm, LoginForm
from my_app.models import User, Post



posts = [

    {
        'author':  'Corey Schafer',
        'title': 'Bog Post 1',
        'content': 'First post content',
        'date_posted': 'april 20, 2018'
    },
    {

        'author':  'jane Doe',
        'title': 'Bog Post 2',
        'content': 'Second post content',
        'date_posted': 'april 21, 2018'
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account crated for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "thisismazhar@gmail.com" and form.password.data == 'laila':
            flash("Loged n succefully!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Not Logged in, pls check email and assword")
    return render_template('login.html', title='Login', form=form)
