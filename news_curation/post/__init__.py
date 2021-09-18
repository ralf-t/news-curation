from flask import Blueprint

bp = Blueprint("post", __name__)

from news_curation.post import routes, models