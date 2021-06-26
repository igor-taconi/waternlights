from typing import NoReturn

from flask import Blueprint, Flask

from app.config import static_folder, template_folder
from .views import about, contact, index

pages = Blueprint(
    'pages',
    __name__,
    template_folder=template_folder,
    static_folder=static_folder,
    url_prefix='/',
)

pages.add_url_rule('/', view_func=index)
pages.add_url_rule('/contato', view_func=contact)
pages.add_url_rule('/sobre', view_func=about)


def init_app(app: Flask) -> NoReturn:
    app.register_blueprint(pages)
