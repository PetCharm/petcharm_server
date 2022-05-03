import requests

url = 'http://43.138.31.99:10002/'
secret = 'petcharmsecretestkey9283'


def register(username):
    api = 'auth/user_register'
    body = {
        "secret": secret,
        "platform": 1,
        "userID": username,
        "nickname": username,
        "operationID": "123111111"
    }
    r = requests.post(url + api, json=body)
    return r.json()['data']['token']


def get_token(username):
    api = 'auth/user_token'
    body = {
        "secret": secret,
        "platform": 1,
        "userID": username,
        "operationID": "123111111"
    }
    r = requests.post(url + api, json=body)
    return r.json()['data']['token']
