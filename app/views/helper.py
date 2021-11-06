from app import app
import jwt
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
from .users import user_by_username
import datetime


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'mensagem': 'nao foi possivel verificar', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    user = user_by_username(auth.username)
    if not user:
        return jsonify({'mensagem': 'usuario nao encontrado', 'data': {}}), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'mensagem': 'Validado com sucesso', 'token': token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'mensagem': 'nao foi possivel verificar', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'mensagem': 'falta o token', 'data': {}}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = user_by_username(username=data['username'])
        except Exception as e:
            print(e)
            return jsonify({'mensagem': 'token invalido ou expirado', 'data': {}}), 401
        return f(current_user, *args, **kwargs)
    return decorated