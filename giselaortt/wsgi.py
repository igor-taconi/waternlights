from .app import create_app
from dotenv import load_dotenv


load_dotenv('../.flaskenv')
app = create_app()
