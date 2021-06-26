from typing import NoReturn

from flask import Flask
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.peewee import ModelView
from flask_simplelogin import login_required, SimpleLogin

from app.database.models import Post, PostCategory, User
from .auth import verify_login
from .models import PostAdmin, UserAdmin

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)
admin = Admin()


def init_app(app: Flask) -> NoReturn:
    SimpleLogin(app, login_checker=verify_login)
    admin.name = app.config.FLASK_ADMIN_TITLE
    admin.template_mode = app.config.FLASK_ADMIN_TEMPLATE_MODE
    admin.init_app(app)
    admin.add_view(UserAdmin(User))
    admin.add_view(PostAdmin(Post))
    admin.add_view(ModelView(PostCategory))
