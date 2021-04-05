from flask import Blueprint

from .views import about, blog, index, login, store

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/store", view_func=store)
bp.add_url_rule("/login", view_func=login, endpoint="login")
bp.add_url_rule("/blog", view_func=blog)
bp.add_url_rule("/about", view_func=about)


def init_app(app):
    app.register_blueprint(bp)
