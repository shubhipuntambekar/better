from flask import Blueprint
from flask_restful import Api

from resource.users import User

routes_bp = Blueprint('routes', __name__)
api = Api(routes_bp)

api.add_resource(User, '/user')
