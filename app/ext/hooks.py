from typing import NoReturn

from flask import Flask

from app.models import Post, User, db


def init_app(app: Flask) -> NoReturn:
    @app.before_first_request
    def _create_tables():
        """Cria as tabelas do banco antes do primeiro request."""
        MODELS = [User, Post]
        db.create_tables(MODELS)

    @app.teardown_request
    def _db_close(exc):
        """Fecha a conexão com o banco se não estiver fechada."""
        if not db.is_closed():
            db.close()
