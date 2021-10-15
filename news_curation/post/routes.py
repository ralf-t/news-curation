from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user

from news_curation.extensions import db
from news_curation.post import bp

from news_curation.post.forms import PostForm
from news_curation.post.models import Post

from news_curation.topic.models import Topic


@bp.route("/")
def home():
    return "post home"

tags = []
@bp.route("/create", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    form.topics.choices = [(g.id, g.topic) for g in Topic.query.order_by('topic')] #choices for the topic dropdown.
    if request.method == 'POST':
        if form.submit.data: #when user clicks the 'Post' button
            if form.validate_on_submit():
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
                dropdown_error = "This topic has already been added!"
                return render_template('post/manage_post.html', form=form, legend='New Post', tags=tags, dropdown_error=dropdown_error)

        elif request.form['tag_to_remove']: #when one of the added tags is clicked (this will remove that tag)
            tag_name = request.form.get('tag_to_remove')
            tags.remove(tag_name)

    return render_template('post/manage_post.html', form=form, legend='New Post', tags=tags)


@bp.route("/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/post.html', post=post)



    return render_template('create_post.html', form=form, legend='Update Post', tags=tags)