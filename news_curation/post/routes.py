from flask_login import login_required

from news_curation.post import bp
from news_curation.post.models import Post

@bp.route("/")
def home():
    return "post home"

@bp.route("/<int:post_id>")
@login_required
def read(post_id):
    post = Post.query.get_or_404(post_id)

    return post.content