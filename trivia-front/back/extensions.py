from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from argon2 import PasswordHasher

db  = SQLAlchemy()

migrate = Migrate()


cors = CORS()


ph = PasswordHasher()
