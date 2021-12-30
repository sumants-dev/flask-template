from enum import unique
from app import db

Model = db.Model
Column = db.Column


class User(Model):
    __tablename__ = "users"
    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String(64), nullable=False)
    last_name = Column(db.String(64), nullable=False)
    email = Column(db.String(64), nullable=False, unique=True)
    phone = Column(db.String(32), nullable=False, unique=True)
    password = Column(db.String(128), nullable=False)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)