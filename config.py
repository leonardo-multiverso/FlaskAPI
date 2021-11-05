import string
import random

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/mediumapi'
SQLALCHEMY_DATABASE_URI = 'sqlite:////home/leonardo/github/FlaskAPI/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key

# lib
# marshmallow-sqlalchemy