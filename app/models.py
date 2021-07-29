# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db
from .utils import base62_decoder, base62_encoder

class URL(db.Model):
    """
    Create URL table
    """

    ___tablename___ = 'urls'

    id = db.Column('id_', db.Integer, primary_key=True)
    original_url = db.Column('original_url', db.String(512))
    short_url = db.Column('short_url', db.String(8), unique=True)

    def __init__(self, original):
        self.original_url = original
        self.short_url = '12345678'
