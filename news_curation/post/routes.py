from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_required, current_user

from news_curation.extensions import db

from news_curation.post import bp
from news_curation.post.models import Post

from news_curation.comment.forms import CommentForm

from news_curation.post.forms import PostForm
from news_curation.post.models import Post

from news_curation.topic.models import Topic, topics


@bp.route("/")
def home():
    return "post home"

# <<<<<<< HEAD
# @bp.route("/<int:post_id>", methods=["POST","GET"])
# @login_required
# def read(post_id):
#     post = Post.query.get_or_404(post_id)

#     form = CommentForm()

#     # if form.validate_on_submit():
#     #     pass

#     return post.content
# =======

tags = []
@bp.route("/create", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    form.topics.choices = [(g.id, g.topic) for g in Topic.query.order_by('topic')] #choices for the topic dropdown.
    dropdown_error = None
    if request.method == 'POST':
        if form.submit.data: #when user clicks the 'Post' button
            if not tags: #if there were no tags added
                dropdown_error = "Tags cannot be empty! Please add at least one."
                return render_template('post/manage_post.html', form=form, legend='New Post', 
                                        tags=tags, dropdown_error=dropdown_error)
            elif form.validate_on_submit():
                post = Post(title=form.title.data, content=form.content.data, author=current_user)
                db.session.add(post) #adds new post to database
                
                for tag in tags: #add selected tags to the post in the database
                    post_tag = Topic.query.filter_by(topic=tag).first()
                    post.topic.append(post_tag)

                db.session.commit()
                del tags[0:] #delete all content of the 'tags' list
                flash('Post has been created!', 'success')
                return redirect(url_for('user.home'))

        elif form.add_topic.data: #when user clicks the 'add topic' button
            #append name of selected choice to a list
            
            topic_name = dict(form.topics.choices).get(form.topics.data)
            try:
                tags.index(topic_name) #checks if a tag is already in the 'tags' list
            except:
                tags.append(topic_name) #appends the selected tag to 'tags' if it is not yet in the list
            else:
                dropdown_error = "This tag has already been added!"
            return render_template('post/manage_post.html', form=form, legend='New Post', 
                                        tags=tags, dropdown_error=dropdown_error)

        elif request.form['tag_to_remove']: #when one of the added tags is clicked (this will remove that tag)
            tag_name = request.form.get('tag_to_remove')
            tags.remove(tag_name)
            return render_template('post/manage_post.html', form=form, legend='New Post', tags=tags)
    
    del tags[0:]
    return render_template('post/manage_post.html', form=form, legend='New Post')


#viewing a single post
@bp.route("/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/post.html', post=post)

tags_to_remove = []
@bp.route("<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    # tags = []
    post = Post.query.get_or_404(post_id)
    if post.author != current_user: #if logged-in user is not the author of post, abort
        abort(403)

    form = PostForm()
    form.topics.choices = [(g.id, g.topic) for g in Topic.query.order_by('topic')] #choices for the topic dropdown.
    dropdown_error = None

    if request.method == 'POST':
        if form.submit.data and form.validate_on_submit(): #updates the post
            if not tags: #if there were no tags added
                dropdown_error = "Tags cannot be empty! Please add at least one."
                return render_template('post/manage_post.html', form=form, legend='Update Post', 
                                        tags=tags, dropdown_error=dropdown_error)
            post.title = form.title.data
            post.content = form.content.data
            for tag in tags_to_remove:
                tag_row = Topic.query.filter_by(topic=tag).first() #gets the row of selected tag in Topic table
                if tag_row in post.topic:
                    post.topic.remove(tag_row)

            for tag in tags: #add selected tags to the post in the database
                tag_row = Topic.query.filter_by(topic=tag).first() #gets the row of selected tag in Topic table
                #if selected tag is not yet associated to the post
                if tag_row not in post.topic: #prevents duplicate rows in topics table
                    post.topic.append(tag_row)
            
            db.session.commit()
            del tags[0:] #delete all content of the 'tags' list
            del tags_to_remove[0:]
            flash('Post has been updated!', 'success')
            return redirect(url_for('post.post', post_id=post.id))

        elif form.add_topic.data: #when user clicks the 'add topic' button
            #append name of selected choice to a list
            topic_name = dict(form.topics.choices).get(form.topics.data)
            try:
                tags.index(topic_name) #checks if a tag is already in the 'tags' list
            except:
                tags.append(topic_name) #appends the selected tag to 'tags' if it is not yet in the list
            else:
                dropdown_error = "This tag has already been added!"
                return render_template('post/manage_post.html', form=form, legend='Update Post',
                                        tags=tags, dropdown_error=dropdown_error)

        elif request.form['tag_to_remove']: #when one of the added tags is clicked (this will remove that tag)
            tag_name = request.form.get('tag_to_remove')
            tags_to_remove.append(tag_name)
            tags.remove(tag_name)

    elif request.method == 'GET': #displays the data of the post when page is opened
        form.title.data = post.title
        form.content.data = post.content
        del tags[0:]
        for topic in post.topic:   
            tags.append(topic.topic)

    return render_template('post/manage_post.html', title='Update Post', form=form, legend='Update Post', tags=tags)


@bp.route("/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('user.profile'))


# Saving post
@bp.route("/<int:post_id>/save")
@login_required
def save_post(post_id):
	home = request.args.get('home')
	post = Post.query.get_or_404(post_id)

	if current_user in post.saved_by:	# if user has already saved the post
	    flash('Post is already in Saved Posts', 'info')
	else:
	    post.saved_by.append(current_user)
	    db.session.commit()
	    flash('Post has been saved!', 'success')

	if home == 'True': #return to homepage if saved from there
		return redirect(url_for('user.home', _anchor=post_id))
	elif home == 'Profile':
		return redirect(url_for('user.profile', _anchor=post_id))
	elif home == 'Popular':
		return redirect(url_for('user.popular', _anchor=post_id))
	else:
		return redirect(url_for('post.post', post_id=post_id))


# Removing saved post
@bp.route("/<int:post_id>/remove_saved")
@login_required
def remove_saved(post_id):
	home = request.args.get('home')

	post = Post.query.get_or_404(post_id)
	post.saved_by.remove(current_user)
	db.session.commit()
	flash('Post removed from Saved Posts', 'info')

	if home == 'True': #return to homepage if saved from there
		return redirect(url_for('user.home', _anchor=post_id))
	elif home == 'Saves':
		return redirect(url_for('user.saved_posts'))
	elif home == 'Profile':
		return redirect(url_for('user.profile', _anchor=post_id))
	elif home == 'Popular':
		return redirect(url_for('user.popular', _anchor=post_id))
	else:
		return redirect(url_for('post.post', post_id=post_id))


#Liking post
@bp.route("/<int:post_id>/like")
@login_required
def like_post(post_id):
	home = request.args.get('home')

	post = Post.query.get_or_404(post_id)
	# post.likes += 1
	# db.session.commit()

	if current_user not in post.liker:
		post.liker.append(current_user)
		if current_user in post.disliker: #if current user dislikes the post, remove dislike
			post.disliker.remove(current_user)
	else:
		post.liker.remove(current_user)
	
	db.session.commit()

	if home == 'True': #return to homepage if liked from there
		return redirect(url_for('user.home', _anchor=post_id))
	elif home == 'Saves':
		return redirect(url_for('user.saved_posts', _anchor=post_id))
	elif home == 'Profile':
		return redirect(url_for('user.profile', _anchor=post_id))
	elif home == 'Popular':
		return redirect(url_for('user.popular', _anchor=post_id))
	else:
		return redirect(url_for('post.post', post_id=post_id))

#Disliking post
@bp.route("/<int:post_id>/dislike")
@login_required
def dislike_post(post_id):
	home = request.args.get('home')

	post = Post.query.get_or_404(post_id)

	if current_user not in post.disliker: #if user is first time disliker, add to db
		post.disliker.append(current_user)
		if current_user in post.liker: #if current user likes the post, remove like
			post.liker.remove(current_user)
	else:
		post.disliker.remove(current_user)
	
	db.session.commit()

	if home == 'True': #return to homepage if disliked from there
		return redirect(url_for('user.home', _anchor=post_id))
	elif home == 'Saves':
		return redirect(url_for('user.saved_posts', _anchor=post_id))
	elif home == 'Profile':
		return redirect(url_for('user.profile', _anchor=post_id))
	elif home == 'Popular':
		return redirect(url_for('user.popular', _anchor=post_id))
	else:
		return redirect(url_for('post.post', post_id=post_id))
