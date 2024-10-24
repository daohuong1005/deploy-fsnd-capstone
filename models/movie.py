from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from models.database import db

class Movie(db.Model):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)
    actors = relationship('Actor', backref="movie", lazy=True)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': list(map(lambda actor: actor.format(), self.actors))
        }
    def __repr__(self):
        return f'<Movie {self.name}>'
