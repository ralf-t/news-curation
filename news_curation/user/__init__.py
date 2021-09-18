from flask import Blueprint

bp = Blueprint("user", __name__)

from news_curation.user import routes, models
