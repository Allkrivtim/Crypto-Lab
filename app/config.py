import os
from fastapi.templating import Jinja2Templates

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
API_TOKEN = os.getenv('API_TOKEN', '7282216904:AAEXeOdSIA2m8nT_x1AYa74r8EdTdQSN9Ak')
NGROK_URL = os.getenv('NGROK_URL', 'https://5684-77-238-244-231.ngrok-free.app')
COMMUNITY_LINK = os.getenv('COMMUNITY_LINK', 'https://t.me/cryptolabgamecommunity')
templates = Jinja2Templates(directory="app/templates")
staticfiles_path = os.path.join(os.path.dirname(__file__), "static")