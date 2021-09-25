from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required

from news_curation.extensions import bcrypt, db

from news_curation.user import bp
from news_curation.user.forms import LoginForm, RegistrationForm
from news_curation.user.models import User, user_interests

from news_curation.post.models import Post
from news_curation.topic.models import Topic, topics


@bp.route("/")
def home():

    # can be also done using only one if and return

    if current_user.is_authenticated: #posts are only filtered for logged-in users; anonymouse users see all posts
        # join all tables then filter posts by the interests of current user
        posts = Post.query.join(topics, Post.id == topics.c.post_id).join(user_interests, topics.c.topic_id == user_interests.c.topic_id).filter_by(user_id=current_user.id)

        return render_template('user/home.html', posts=posts)
    else:
        posts = Post.query.all()
        return render_template('user/home.html', posts=posts)

@bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:   #prevents logged-in user from going to register page
        return redirect(url_for('user.home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        #generate hashed password for the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password
            )
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('user.login'))

    return render_template('user/register.html', form=form)



@bp.route("/login", methods=['GET', 'POST'])
def login():
    
    #prevents logged-in user from going to login page
    if current_user.is_authenticated:
        flash('You are already logged in.', 'success')
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

@bp.route("/profile")
@login_required     #prevents anonymous user from going to profile page
def profile():
    return render_template('user/profile.html')
