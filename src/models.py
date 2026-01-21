from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    user_name =  Column(String(250), nullable=False)
    first_name =  Column(String(250), nullable=False)
    second_name =  Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

  
class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True)
    comment_text =  Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("User.id"))
    post_id = Column(Integer, ForeignKey("Post.id"))
    comment_relationship = relationship("Post")


class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    post_relationship = relationship("User")


class Media(Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("Post.id"))
    post_relationship = relationship("Post")


class Follower(Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("User.id"))
    user_to_id = Column(Integer, ForeignKey("User.id"))
    user_relationship_from = relationship("User", foreign_keys=[user_from_id])
    user_relationship_to = relationship("User", foreign_keys=[user_to_id])

