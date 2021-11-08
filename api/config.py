import string
import random

chave_randomica = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(chave_randomica) for i in range(12))

DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'mysql://<usuarioi>:<senha>@localhost:3306/<database>'
SQLALCHEMY_DATABASE_URI = 'sqlite:////home/leonardo/github/FlaskAPI/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key