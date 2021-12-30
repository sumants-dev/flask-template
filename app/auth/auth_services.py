from flask import make_response
from flask_jwt_extended import create_access_token
from app.models import User
from app import db
import bcrypt

class User_Services:
    @staticmethod
    def login(email: str, password: str):
        user = User.query.filter_by(email=email).first() 
        
        if user is None:
            return "Unknown Email or Password", 404
        
        print(user.password)
        if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return "Unknown Email or Password", 404
        
        response = make_response({"msg": "Logged In", "ACCESS_TOKEN": create_access_token(email)}, 200)
        return response


    @staticmethod
    def register(first_name: str, last_name: str, email: str, phone: str, password: str):
          
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        hashed = hashed.decode("utf-8")
        new_user = User(first_name = first_name, last_name = last_name, email = email, phone = phone, password = hashed)
        db.session.add(new_user)
        db.session.commit()

        response = make_response({"msg": "SUCESSFULLY REGISTERED", "ACCESS_TOKEN": create_access_token(email)}, 200)
        return response