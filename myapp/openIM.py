import requests

url = 'http://43.138.31.99:10002/'
secret = '"tuoyun"'


def register(user):
    api = 'auth/user_register'
    body = {
        "secret": secret,
        "platform": 1,
        "userID": user.username,
        "nickname": user.username,
        "operationID": "123111111"
    }
    r = requests.post(url + api, json=body)
    return r.json()['data']['token']
