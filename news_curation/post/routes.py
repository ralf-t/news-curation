from news_curation.post import bp

@bp.route("/")
def home():
    return "post home"