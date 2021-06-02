from sqlalchemy.orm import Session
from flask import Blueprint, render_template, abort, request
import json

from models import User
from crypt import bcrypt
import db


wrap = Blueprint('wrap', __name__)

@wrap.route('/signup', methods=['POST'])
def signup():
    data = json.loads(request.data)
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        abort(401, 'введите логин и пароль')
    user = db.session.query(User).filter_by(login=login).first()

    if user:
        abort(401, 'пользователя не существует') 
    
    new_user = User(user_id, first_name, last_name, email,login, password)
    db.session.add(new_user)
    db.session.commit()

    return {'messeg': 'ok'}
    

@wrap.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)
    except Exception as e:
        data= {}
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        abort(401, 'введите логин и пароль')
    user = db.session.query(User).filter_by(login=login).first()

    if not user:
        abort(401, 'пользователя не существует')

    check_password = bcrypt.check_password_hash(user.password, password)

    if not check_password:
        abort(401, 'неверный пароль')
    
    return {'messeg': 'ok'}
