import requests
import json


# {'token': '88b1a2687fc3ff1e3b62ecc670560c5c6fef8d2f', 'user_id': 2, 'email': 'tony@gmail.com'}
url = 'http://127.0.0.1:8000/api/actor/'
# url = 'http://127.0.0.1:8000/api/user/auth-token/'

payload = {'username': 'tony@gmail.com', 'password':'loverboy'}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 88b1a2687fc3ff1e3b62ecc670560c5c6fef8d2f'
}
r = requests.get(url, data=json.dumps(payload), headers=headers)

print(r.json())