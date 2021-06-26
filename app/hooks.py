from typing import NoReturn

from flask import Flask

from app.database import db
from app.database.models import Post, PostCategory, User


def init_app(app: Flask) -> NoReturn:
    @app.before_first_request
    def _create_tables():
        '''Cria as tabelas do banco antes do primeiro request.'''
        MODELS = [Post, PostCategory, User]
        db.create_tables(MODELS)

    @app.teardown_request
    def _db_close(exc):
        '''Fecha a conexão com o banco se não estiver fechada.'''
        if not db.is_closed():
            db.close()
