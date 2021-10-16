from flask_login import login_required

from news_curation.post import bp
from news_curation.post.models import Post

from news_curation.comment.forms import CommentForm

@bp.route("/")
def home():
    return "post home"

@bp.route("/<int:post_id>", methods=["POST","GET"])
@login_required
def read(post_id):
    post = Post.query.get_or_404(post_id)

    form = CommentForm()

    # if form.validate_on_submit():
    #     pass

    return post.content