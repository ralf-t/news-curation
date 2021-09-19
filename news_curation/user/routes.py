from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, logout_user

from news_curation.extensions import bcrypt

from news_curation.user import bp
from news_curation.user.forms import LoginForm
from news_curation.user.models import User

@bp.route("/")
def home():
    return "user home"

@bp.route("/login", methods=['GET', 'POST'])
def login():
    
    #prevents logged-in user from going to login page
    if current_user.is_authenticated:   
        return redirect(url_for('user.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #when logged-out users access restricted pages, they will be redirected
            #to login. After logging in, they will be redirected to the page they wanted to access(next_page)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('user.home'))
        
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')

    return render_template('user/login.html', form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('user.home'))