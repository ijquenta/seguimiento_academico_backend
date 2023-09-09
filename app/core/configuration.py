import os

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
# SQLALCHEMY_DATABASE_URL =os.getenv('SQLALCHEMY_DATABASE_URL','postgresql://postgres:gimena@127.0.0.1:5432/aguinaldo_db')
# SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL','postgresql://usu_reintegro:u5u_r3in73gR0@200.7.161.176:5432/bd_reintegro')
# SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL','postgresql://usu_bsocialdocente:usu_bsocialdocente@200.7.161.176:5432/bd_bsocialdocente')
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL','postgresql://ijquenta:123456@localhost:5432/b_academico')
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "secret")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "confidential")
TOKEN_MINUTES_LIFE_ADMIN=os.getenv("DBUSER", 60)

API_SECRET_KEY = os.getenv("API_SECRET_KEY", "f")
API_URL = os.getenv("API_URL", "f")

SERVER_HOST = os.environ.get("SERVER_HOST", '0.0.0.0') 
SERVER_PORT = int(os.environ.get("SERVER_PORT", "5001"))
DEBUG = os.environ.get("DEBUG", "false") == "true"

DB_AGUINALDO = os.environ.get("DB_AGUINALDO", '')

URL_REGULAR = os.environ.get("URL_REGULAR", 'http://0.0.0.0:5000/regular_api')

API_SECRET_KEY = os.getenv("API_SECRET_KEY", "DofluFngQjGpedWvVY1A8uyplHId-b6L")

# Configurar a la IP del WebService -> 200.7.161.170:5000/api_v2
WS_API_URL = os.getenv("WS_API_URL", "http://200.7.161.170:5000/api_v2")
#WS_API_URL = os.getenv("WS_API_URL", "http://0.0.0.0:5000/api_v2")


