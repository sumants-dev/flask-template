from app import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix = "/auth")

from . import auth_controller
