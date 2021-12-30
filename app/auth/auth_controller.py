from marshmallow import fields
from . import auth_bp
from flask import request
from flask.views import MethodView
from .auth_services import User_Services
from app import ma

class User_Login_Schema(ma.Schema):
    class Meta:
        fields = ("email", "password")

class User_Registeration_Schema(ma.Schema):
    class Meta:
        fields = ("first_name", "last_name", "email", "phone", "password") 


@auth_bp.route("/register")
class Register(MethodView):
    @auth_bp.arguments(User_Registeration_Schema)
    def post(self, data):
        return User_Services.register(**data)


@auth_bp.route("/login")
class Login(MethodView):
    @auth_bp.arguments(User_Login_Schema)
    def post(self, data):
        return User_Services.login(**data)