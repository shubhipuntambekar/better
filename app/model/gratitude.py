from peewee import TextField

from app.model.base import BaseModel


class Gratitude(BaseModel):
    content = TextField()
    keywords_list = TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(Gratitude, *args, **kwargs)
