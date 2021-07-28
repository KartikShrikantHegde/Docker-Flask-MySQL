from flask import Blueprint, redirect

from app import db
from .models import URL

short = Blueprint('short', __name__)


@short.route('/<short_url>')
def redirect_to_url(short_url):
  original_url = URL.query.filter_by(short_url=short_url).first_or_404()
  if original_url:
    redirect(original_url.original)
  else:
    return f'<h1>URL does not exist</h1>'



