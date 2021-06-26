from datetime import datetime

import peewee as pw
from slugify import slugify

from app.database import BaseModel


class BaseCategory(BaseModel):
    category = pw.CharField()


class User(BaseModel):
    username = pw.CharField(max_length=80)
    email = pw.CharField(max_length=120)
    password = pw.TextField()


class PostCategory(BaseCategory):
    ...


class Post(BaseModel):
    title = pw.CharField(max_length=120)
    text = pw.TextField()
    update_at = pw.DateTimeField(default=datetime.now)
    slug = pw.CharField(max_length=120)
    user = pw.ForeignKeyField(User, backref='post', null=True)
    category = pw.ForeignKeyField(PostCategory, backref='post', null=True)

    class Meta:
        order_by = ('-update_at',)

    def __init__(self, *args, **kwargs):
        kwargs['slug'] = slugify(kwargs.get('title', ''))
        # kwargs['update_at'] = datetime.now()
        super().__init__(*args, **kwargs)


class IlustrationCategory(BaseCategory):
    ...


class Ilustration(BaseModel):
    title = pw.CharField()
    image = pw.TextField()
    creation_date = pw.DateTimeField(null=True, default=datetime.now)
    inserted_at = pw.DateTimeField(default=datetime.now)
    decription = pw.TextField(null=True)
    slug = pw.CharField()
    category = pw.ForeignKeyField(
        IlustrationCategory, backref='ilustration', null=True
    )

    def __init__(self, *args, **kwargs):
        kwargs['slug'] = slugify(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)
