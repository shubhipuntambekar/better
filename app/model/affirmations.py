from peewee import TextField

from app.model.base import BaseModel


class Affirmations(BaseModel):
    content = TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(Affirmations, *args, **kwargs)