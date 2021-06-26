from typing import NoReturn

from flask import Blueprint, Flask

from app.config import static_folder, template_folder
from .views import detail, list

ilustrations = Blueprint(
    'ilustrations',
    __name__,
    template_folder=template_folder,
    static_folder=static_folder,
    url_prefix='/ilustratacoes'
)

ilustrations.add_url_rule('/', view_func=list)
ilustrations.add_url_rule('/<slug>', view_func=detail)


def init_app(app: Flask) -> NoReturn:
    app.register_blueprint(ilustrations)
