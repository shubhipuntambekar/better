from marshmallow import Schema, fields


class RegisterSchema(Schema):
    email_id = fields.Email(required=True, strict=True)


class ValidateSchema(Schema):
    email_id = fields.Email(required=True, strict=True)
    otp = fields.Integer(required=True)
