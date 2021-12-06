from flask import redirect, url_for

from news_curation.main import bp

@bp.route("/")
def home():
    return redirect(url_for("user.home"))