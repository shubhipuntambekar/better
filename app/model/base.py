import os
from datetime import datetime

from peewee import Model, AutoField, CharField, DateTimeField, MySQLDatabase

database = MySQLDatabase(os.getenv('DB_NAME'),
                         user=os.getenv('DB_USER'),
                         password=os.getenv('DB_PASSWORD'),
                         host=os.getenv('DB_HOST'))


class BaseModel(Model):
    id = AutoField()
    created_by = CharField(max_length=30, default="system")
    created_at = DateTimeField(default=datetime.now)
    updated_by = CharField(max_length=30, default="system")
    updated_at = DateTimeField(default=datetime.now)

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        database.create_tables([model])

    class Meta:
        database = database


