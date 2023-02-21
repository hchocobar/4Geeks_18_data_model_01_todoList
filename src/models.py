import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), unique=True, nullable=False)
    lastname = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    # Relationship
    posts = relationship("Post", backref="user", lazy=True)
    comments = relationship("Comment", backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    # FK and relationships
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    medias = relationship("Media", backref="post", lazy=True)
    comments = relationship("Comment", backref="post", lazy=True)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    url = Column(String(250), nullable=False)
    # FK and relationships
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    # FK and relationships
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user = relationship(User)
    post = relationship(Post)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    # FK and relationships
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
