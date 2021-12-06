from flask import Blueprint

bp = Blueprint("main", __name__)

from news_curation.main import routes
