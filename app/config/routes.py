from flask import Blueprint
from flask_restful import Api

from app.resource.onboard import RegisterResource, ValidateResource

routes_bp = Blueprint('routes', __name__)
api = Api(routes_bp)

api.add_resource(RegisterResource, '/register')
api.add_resource(ValidateResource, '/validate')
