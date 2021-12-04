#imports for profile picture
import os
import secrets  #for creating random hex for picture filename
from PIL import Image  #from Pillow package
#####

from flask import render_template, url_for, flash, redirect, request, current_app
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import desc

from news_curation.extensions import bcrypt, db

from news_curation.user import bp
from news_curation.user.forms import LoginForm, RegistrationForm, UpdateProfileForm
from news_curation.user.models import User, user_interests

from news_curation.post.models import Post
from news_curation.topic.models import Topic, topics


@bp.route("/")
@bp.route("/home")
def home():

    # can be also done using only one if and return

    if current_user.is_authenticated: #posts are only filtered for logged-in users; anonymouse users see all posts
        # join all tables then filter posts by the interests of current user
        user = User.query.filter_by(id=current_user.id).first()
        
        # for checking if a user has selected topics of interest
        ctr = 0
        for interest in user.topics_of_interest:
            ctr += 1
        
        if ctr >= 1:
            posts = Post.query.join(topics, Post.id == topics.c.post_id).join(user_interests, topics.c.topic_id == user_interests.c.topic_id).filter_by(user_id=current_user.id).order_by(desc(Post.created_at))
        else:
            posts = Post.query.order_by(desc(Post.created_at)).all()
    else:
        posts = Post.query.order_by(desc(Post.created_at)).all()
    
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
            flash('Login Unsuccessful. Please check your username and password.', 'danger')

    return render_template('user/login.html', form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('user.home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename) #split the picture's filename and extension
    picture_fn = random_hex + f_ext #this will be the filename of picture when saved    
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@bp.route("/profile", methods=['GET', 'POST'])
@login_required     #prevents anonymous user from going to profile page
def profile():
    user_posts = Post.query.filter_by(user_id=current_user.id).all()
    form = UpdateProfileForm()
    error = False
        
    if form.validate_on_submit():
        if form.picture.data:   #if a picture was uploaded
            picture_file = save_picture(form.picture.data)
            current_user.profile_picture = picture_file     #save the picture file to database
        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            current_user.password = hashed_password

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile successfully updated!', 'success')
        return redirect(url_for('user.profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.username.data = current_user.username
        form.email.data = current_user.email
    else:
        error = True

    image_file = url_for('static', filename='profile_pics/' + current_user.profile_picture)
    return render_template('user/profile.html', user_posts=user_posts, 
                            form=form, error=error, image_file=image_file)


@bp.route("/saved_posts")
@login_required
def saved_posts():
    posts = current_user.saved_posts
    return render_template('user/saved_posts.html', posts=posts)
