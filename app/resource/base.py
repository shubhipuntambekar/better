from flask import jsonify
from flask_restful import Resource


class BaseResource(Resource):
    error_response_schema = {
        'error': {
            'code': None,
            'message': None
        }
    }

    success_response_schema = {
        'data': None,
        'message': None
    }

    def handle_error(self, code, message):
        self.error_response_schema['error']['code'] = code
        self.error_response_schema['error']['message'] = message
        response = jsonify(self.error_response_schema)
        response.status_code = code
        return response

    def handle_success(self, data, message):
        self.success_response_schema['data'] = data
        self.success_response_schema['message'] = message
        response = jsonify(self.success_response_schema)
        return response
