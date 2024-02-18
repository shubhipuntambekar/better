import os
from functools import wraps

import jwt
from flask import request, jsonify


def authenticate(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        bearer_token = request.headers.get('Authorization')
        if not bearer_token:
            response = jsonify({'message': 'Missing auth token'})
            response.status_code = 401
            return response
        try:
            token = bearer_token.replace("Bearer ", "")
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
        except Exception as e:
            print('Exception occurred: ', e)
            response = jsonify({'message': 'Invalid token'})
            response.status_code = 403
            return response

        return function(*args, **kwargs)

    return wrapper
