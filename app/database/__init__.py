from datetime import datetime

import peewee as pw

from ..config import settings


db = pw.SqliteDatabase('database.db')
# db = pw.PostgresqlDatabase(
#     database=settings.get_environ('DB_NAME'),
#     user=settings.get_environ('DB_USER'),
#     password=settings.get_environ('DB_PASSWORD'),
#     host=settings.get_environ('DB_HOST'),
#     port=settings.get_environ('DB_PORT'),
#     autorollback=True,
# )


class BaseModel(pw.Model):
    create_at = pw.DateTimeField(default=datetime.now)

    class Meta:
        database = db
