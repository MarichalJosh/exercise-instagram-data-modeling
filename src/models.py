import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) 
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(80), nullable=False)
    picture = Column(String())
    user = relationship('Post', back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    date = Column(String(25))
    likes = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id')) 
    media = relationship("Media", uselist=False, back_populates="post")
    comment = relationship("Comment", uselist=False, back_populates="post")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String())
    description = Column(String(300), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    commentText = Column(String(300), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')