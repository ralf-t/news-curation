from flask import Blueprint

bp = Blueprint("comment", __name__)

from news_curation.comment import routes, models