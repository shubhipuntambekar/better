from peewee import CharField, DateTimeField, TextField

from app.model.base import BaseModel


class User(BaseModel):

    email_id = CharField(max_length=100)
    user_name = CharField(max_length=30, null=True)
    affirmations_time = DateTimeField(null=True)
    gratitude_time = DateTimeField(null=True)
    sent_affirmation_list = TextField(null=True)
    sent_gratitude_list = TextField(null=True)
    excluded_gratitude_keyword_list = TextField(null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(User, *args, **kwargs)

    @classmethod
    def create_user(cls, user_details):
        user = User.select().where(User.email_id == user_details.get('email_id'))
        if user:
            print("user already exists.")
            return

        user = User(email_id=user_details.get('email_id', None),
                    user_name=user_details.get('user_name', None),
                    affirmations_time=user_details.get('affirmations_time', None),
                    gratitude_time=user_details.get('gratitude_time', None),
                    sent_affirmation_list=user_details.get('sent_affirmation_list', None),
                    sent_gratitude_list=user_details.get('sent_gratitude_list', None),
                    excluded_gratitude_keyword_list=user_details.get('excluded_gratitude_keyword_list', None))
        user.save()
        print("user created successfully")
