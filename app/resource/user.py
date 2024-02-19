from flask import request
from marshmallow import ValidationError

from app.model.user import User
from app.resource.auth import authenticate
from app.resource.base import BaseResource
from app.schema.request_schema import UserSchema


class UserResource(BaseResource):

    @authenticate
    def put(self):
        request_data = request.get_json()
        schema = UserSchema()

        try:
            user_data = schema.load(request_data)
        except ValidationError as e:
            return self.handle_error(400, e.messages)

        User().update_user(user_data)
        return self.handle_success(user_data, "User update successfully!")
