import requests
import json

# url = 'http://127.0.0.1:8000/users/change-password/'
# url = 'http://127.0.0.1:8000/users/password_reset/confirm/'
# url = "http://127.0.0.1:8000/api/videos/1/likes/"
url = 'http://127.0.0.1:8000/api/user/auth-token/'

payload = {'username': 'love@gmail.com', 'password':'propensity'}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token e4a9f5a38324352b1d9c666da61aafdd70642e44'
}
r = requests.post(url, data=payload)

print(r.json())