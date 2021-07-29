from flask import Blueprint, redirect, url_for, render_template
from flask.globals import request

from .extensions import db
from .models import URL
from .utils import base62_decoder, base62_encoder

short = Blueprint('short', __name__)

@short.route('/', methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    url_received = request.form['nm']
    found_url = URL.query.filter_by(original_url=url_received).first()
    if found_url:
      return redirect(url_for('display_short_url', url=found_url.short_url))
    else:
      new_url = URL(url_received)
      db.session.add(new_url)
      db.session.commit()
      # print(new_url.id)
      
      # return redirect(url_for("display_short_url", url=new_url.short_url))
      return new_url.short_url
  else:
    return render_template('url_page.html')

@short.route('/<short_url>')
def redirect_to_url(short_url):
  original_url = URL.query.filter_by(short_url=short_url).first()
  if original_url:
    redirect(original_url.original)
  else:
    return 'URL does not exist'

@short.route('/display/<url>')
def display_short_url(url):
    return render_template('short_url.html', short_url_display=url)

