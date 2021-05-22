from flask_admin.contrib.peewee import ModelView
from werkzeug.security import generate_password_hash

from app.controllers import date_formatters
from app.models import PostCategory, User


class UserAdmin(ModelView):
    column_list = ['username']
    can_edit = False

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


class PostAdmin(ModelView):
    column_exclude_list = ('id', 'text')

    column_labels = dict(
        title='Título',
        create_at='Data de Publicação',
        update_at='Data de Atualização',
        category='Categoria',
        user='Usuário',
    )

    column_formatters = dict(
        category=lambda w, x, y, z: y.category.category,
        user=lambda w, x, y, z: y.user.username,
    )

    column_type_formatters = date_formatters

    column_default_sort = ('create_at', True)

    column_sortable_list = ("title", "title", "update_at")

    column_searchable_list = ("title", User.username, PostCategory.category)

    column_filters = ("title", "create_at", User.username)

    form_columns = ('title', 'text', 'category', 'user')

    form_ajax_refs = {"user": {"fields": (User.username, "email")}}
