from datetime import datetime

import peewee as pw
from slugify import slugify

from app.config import settings

db = pw.SqliteDatabase("database.db")
# db = pw.PostgresqlDatabase(
#     database=settings.get_environ("DB_NAME"),
#     user=settings.get_environ("DB_USER"),
#     password=settings.get_environ("DB_PASSWORD"),
#     host=settings.get_environ("DB_HOST"),
#     port=settings.get_environ("DB_PORT"),
#     autorollback=True,
# )


class BaseModel(pw.Model):
    class Meta:
        database = db


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
    create_at = pw.DateTimeField(default=datetime.now)
    update_at = pw.DateTimeField(default=datetime.now)
    slug = pw.CharField(max_length=120)
    user = pw.ForeignKeyField(User, backref="post", null=True)
    category = pw.ForeignKeyField(PostCategory, backref="post", null=True)

    class Meta:
        order_by = ("-update_at",)

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
