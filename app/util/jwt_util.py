import os
from datetime import datetime, timedelta

import jwt


class JWTUtil:

    def __init__(self):
        self.secret_key = os.getenv('SECRET_KEY')

    def get_auth_token(self, email_id):
        token = jwt.encode({
            'user': email_id,
            'expiration': str(datetime.utcnow() + timedelta(60))
        }, self.secret_key)

        return token

    def validate_auth_token(self, token):
        try:
            data = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return data
        except Exception as e:
            raise e
