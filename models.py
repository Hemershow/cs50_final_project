# Define database models


from sqlalchemy.util.compat import dataclass_fields
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Post(db.Model):
    title = db.Column(db.String(140))
    description = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(256))
    id = db.Column(db.Integer, primary_key=True)
    comments = db.relationship('Comment')
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1300))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_name = db.Column(db.String(256))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    posts = db.relationship('Post')


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(150))
    image = db.Column(db.String(150))
    posts = db.relationship('Post')
