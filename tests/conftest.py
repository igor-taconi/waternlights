import pytest
from giselaortt.app import create_app, minimal_app


@pytest.fixture(scope='module')
def app():
    """Instance of Main flask app."""
    return create_app()
