import random

from flask import request
from marshmallow import ValidationError

from app.config.redis import RedisManager
from app.resource.base import BaseResource
from app.schema.request_schema import RegisterSchema, ValidateSchema
from app.util.email_util import deliver_email


class RegisterResource(BaseResource):

    def post(self):
        request_data = request.get_json()
        schema = RegisterSchema()

        try:
            register_data = schema.load(request_data)
        except ValidationError as e:
            return self.handle_error(400, e.messages)

        email_id = register_data.get('email_id')
        otp = random.randint(1000, 9999)

        redis_client = RedisManager.get_redis_client()
        redis_client.set(email_id, otp)
        redis_client.expire(email_id, 1200)  # 20 minutes

        deliver_email(email_id, otp)
        return self.handle_success(register_data, 'OTP sent successfully')


class ValidateResource(BaseResource):

    def post(self):
        request_data = request.get_json()
        schema = ValidateSchema()

        try:
            validate_data = schema.load(request_data)
        except ValidationError as e:
            return self.handle_error(400, e.messages)

        redis_client = RedisManager.get_redis_client()

        email_id = validate_data.get('email_id')
        otp = validate_data.get('otp')
        redis_otp = redis_client.get(email_id)

        if redis_otp is None:
            return self.handle_error(400, 'OTP Expired! Please request again.')

        if otp != int(redis_otp):
            return self.handle_error(400, 'Invalid OTP.')

        redis_client.delete(email_id)
        auth_token = random.randbytes(20).hex()
        return self.handle_success(auth_token, 'OTP verification successful!')


