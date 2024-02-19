from marshmallow import Schema, fields


class RegisterSchema(Schema):
    email_id = fields.Email(required=True, strict=True)


class ValidateSchema(Schema):
    email_id = fields.Email(required=True, strict=True)
    otp = fields.Integer(required=True)


class UserSchema(Schema):
    email_id = fields.Email(required=True)
    user_name = fields.Str(required=False)
    affirmations_time = fields.DateTime(required=False)
    gratitude_time = fields.DateTime(required=False)