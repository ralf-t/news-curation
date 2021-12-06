from flask import Blueprint

bp = Blueprint("topic", __name__)

from news_curation.topic import routes, models