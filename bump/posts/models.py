"""Post models

This module contains SQLAlchemy model classes for the posts package.

"""

from bump import DB as db
from bump.posts import constants as POST


class Post(db.Model):
    """Post model class for SQLAlchemy."""

    __tablename__ = 'posts_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(POST.TITLE_LENGTH))
    text = db.Column(db.String(POST.TEXT_LENGTH))
    rating = db.Column(db.Integer)
    time_posted = db.Column(db.DateTime)
    comment_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))

    def __init__(self, title=None, text=None, user_id=None):
        self.title = title
        self.text = text
        self.user_id = user_id

    def get_rating(self):
        return self.rating

    def get_time_posted(self):
        return self.time_posted

    def get_user_id(self):
        return self.user_id

    def get_comment_count(self):
        return self.comment_count

    def __repr__(self):
        return '<Post {title} made by {user_id}>'.format(title=self.title,
                                                         user_id=self.user_id)
