from flask import render_template, url_for, flash, redirect, request
from news_curation import app, db
from news_curation.forms import RegistrationForm, LoginForm
from news_curation.models import User
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:   #prevents logged-in user from going to register page
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                username=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:   #prevents logged-in user from going to login page
        return redirect(url_for('home'))


    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password==form.password.data:
            login_user(user, remember=form.remember.data)
            #when logged-out users access restricted pages, they will be redirected
            #to login. After logging in, they will be redirected to the page they wanted to access(next_page)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')

    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/profile")
@login_required     #prevents anonymous user from going to profile page
def profile():
    return render_template('profile.html')
