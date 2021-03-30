import requests
import json

def test_login():
    data = json.dumps({"login": "qw123", "password": "qwerty"})
    req = requests.post(url='http://127.0.0.1:5000//login', data = data)
    print(req.content)
    content = json.loads(req.content)
    assert content == {'messeg': 'ok'}

def test_login_401():
    data = json.dumps({"login": "qw1234", "password": "qwerty"})
    req = requests.post(url='http://127.0.0.1:5000//login', data = data)
    assert req.status_code == 401



def test_signup():
    data = json.dumps({"user_id": 3, 
                    "first_name": "Andrei",
                    "last_name": "Andreev",
                    "email": "and@mail.ru",
                    "login" : "Andr",
                    "password": "qwerty"})  

    request = requests.post(url='http://127.0.0.1:5000/signup', data = data )
    content = json.loads(request.content)
    assert content == {'messeg': 'ok'}
