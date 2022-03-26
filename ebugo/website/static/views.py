# Store standard routes for site


from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import desc
from .models import Post, Comment, Game
from . import db
import json

# Set views blueprint
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        search = request.form.get('search')
        if search:

            posts = db.session.query(Post, Game).join(Game). \
                filter(Post.title.contains(search)).all()

            return render_template('home.html', user=current_user, posts=posts)

    posts = db.session.query(Post, Game).join(
        Game).order_by(Post.date.desc()).all()

    return render_template('home.html', user=current_user, posts=posts)


@views.route('/bugs', methods=['GET', 'POST'])
@login_required
def bugs():
    posts = db.session.query(Post, Game).join(Game). \
        filter(Post.user_id == current_user.id).all()

    return render_template('bugs.html', user=current_user, posts=posts)


@views.route('/bug/<string:id>', methods=['GET', 'POST'])
@login_required
def bug(id):
    if request.method == 'POST':
        comment = request.form.get('comment')

        if len(comment) < 1:
            flash('Comment is too short.', category='error')
        elif len(comment) > 1300:
            flash('Comment is too big', category='error')
        else:
            new_comment = Comment(
                data=comment, user_name=current_user.user_name, post_id=id,)

            db.session.add(new_comment)
            db.session.commit()
            flash('Comment added!', category='success')

    post = db.session.query(Post, Game).join(Game). \
        filter(Post.id == id).all()

    return render_template('bug.html', result=post, user=current_user)


@views.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    games = Game.query.order_by(Game.game_title.asc())

    if request.method == 'POST':

        title = request.form.get('title')
        description = request.form.get('description')
        gameId = request.form.get('game')

        if len(title) < 1:
            flash('The title is too short :(', category='error')
        elif len(title) > 120:
            flash('The title needs to be under 120 characters', category='error')
        elif len(description) < 10:
            flash('Descrition is too short', category='error')
        elif len(description) > 1300:
            flash('Description needs to be under 1300 characters', category='error')
        else:
            new_post = Post(title=title, description=description,
                            user_id=current_user.id, user_name=current_user.user_name, game_id=gameId)
            db.session.add(new_post)
            db.session.commit()
            flash('Posted!', category='success')

    return render_template('post.html', user=current_user, games=games)


@views.route('/delete-post', methods=['POST'])
def delete_note():
    post = json.loads(request.data)
    postId = post['postId']
    post = Post.query.get(postId)
    comments = Comment.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            if comments:
                db.session.delete(comments)
            db.session.commit()

    return jsonify({})
