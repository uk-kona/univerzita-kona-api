from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', 'sqlite:///' / BASE_DIR / 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
