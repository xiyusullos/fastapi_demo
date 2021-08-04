# coding=utf-8
"""The app package, containing the app factory function."""

import dotenv

dotenv.load_dotenv()

from .main import create_app
