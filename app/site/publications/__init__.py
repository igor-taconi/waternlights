from typing import NoReturn

from flask import Blueprint, Flask

from app.config import static_folder, template_folder
from .views import detail, list

publications = Blueprint(
    'publications',
    __name__,
    template_folder=template_folder,
    static_folder=static_folder,
    url_prefix='/publicacoes'
)

publications.add_url_rule('/', view_func=list)
publications.add_url_rule('/<slug>', view_func=detail)


def init_app(app: Flask) -> NoReturn:
    app.register_blueprint(publications)
