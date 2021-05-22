from datetime import datetime

import peewee as pw

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


class User(BaseModel):
    username = pw.CharField(max_length=80)
    email = pw.CharField(max_length=120)
    password = pw.TextField()


class PostCategory(BaseModel):
    category = pw.CharField(max_length=30)


class Post(BaseModel):
    title = pw.CharField(max_length=120)
    text = pw.TextField()
    create_at = pw.DateTimeField(default=datetime.now)
    update_at = pw.DateTimeField(null=True, default=create_at)
    user = pw.ForeignKeyField(User, backref="post", null=True)
    category = pw.ForeignKeyField(PostCategory, backref="post", null=True)

    class Meta:
        order_by = ("-update_at",)
