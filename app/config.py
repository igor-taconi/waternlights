from os.path import join
from pathlib import Path
from typing import NoReturn

from dynaconf import Dynaconf, FlaskDynaconf
from flask import Flask

settings = Dynaconf(
    envvar_prefix='DYNACONF',
    settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
)

basedir = Path(__file__).resolve().parent.parent

template_folder = join(basedir, 'resources', 'templates')
static_folder = join(basedir, 'resources', 'static')

env_file = join(basedir, '.env')


def init_app(app: Flask) -> NoReturn:
    FlaskDynaconf(app)

