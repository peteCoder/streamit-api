import requests
import json

# url = 'http://127.0.0.1:8000/users/change-password/'
# url = 'http://127.0.0.1:8000/users/password_reset/confirm/'
# url = "http://127.0.0.1:8000/api/videos/1/likes/"
url = 'http://127.0.0.1:8000/api/user/auth-token/'

payload = {'username': 'peter@gmail.com', 'password':'propensity'}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token afbf91b454b50cc56637d34b77133fef3c6604da'
}
r = requests.post(url, data=payload)

print(r.json())