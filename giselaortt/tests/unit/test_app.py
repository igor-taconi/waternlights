from flask import Flask
from giselaortt import app


def test_create_app_must_exist():
    assert hasattr(app, 'create_app'), 'create app does not exist'


def test_creating_app_must_be_invocable():
    assert hasattr(app.create_app, '__call__'), 'creating app is not invocable'


def test_app_is_instance_flask(app):
    assert isinstance(app, Flask), 'create app does not return a flask app'


def test_debug_in_config_is_false(config):
    assert config['DEBUG']


def test_request_return_404(client):
    assert client.get('/url_que_nao_existe').status_code == 404
