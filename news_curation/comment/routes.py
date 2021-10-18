from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_required, current_user

from news_curation.extensions import db

from news_curation.post.models import Post

from news_curation.comment import bp
from news_curation.comment.forms import CommentForm
from news_curation.comment.models import Comment


@bp.route("/add/<int:post_id>", methods=['GET', 'POST'])
@login_required
def add(post_id):
    '''

    Processes commenting to a post.

    Args:
        post_id : id of Post to add comment

    '''

    # fetch post
    post = Post.query.get_or_404(post_id)

    # instantiate form
    form = CommentForm()
    
    # grab form post request
    if form.validate_on_submit():

        # comment entry
        comment = Comment()
        comment.content = form.content.data
        comment.author = current_user
        comment.post = post

        # safe data entry
        try:
            db.session.add(comment)
            db.session.commit()
            flash("Successfully submitted a comment.","success")
            
            return redirect(url_for("post.post",post_id=post.id))

        except:
            flash("An error occured while submitting comment.","danger")

    return render_template('comment/manage_comment.html', form=form)



