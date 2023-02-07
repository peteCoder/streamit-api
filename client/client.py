import requests
import json

# curl -X POST -d "client_id=1OZlPWZurfIzJ0Lx905DUcYqWrxlaIwUizfKxzId&client_secret=TSAmKVn8ZVcqIiAOxeC6OOvVPzw2AkNbIOQJe5BhWeU45h8hcmFe0MS9Nu6cG5IAGyh7S6st655bBHOt28m2AanzoUez7xwTPyRzegTEY4ANhltZYrbfVgrMVs5m5Cla&grant_type=password&username=talk2peteresezobor@gmail.com&password=propensity" http://localhost:8000/auth/token
# {'token': '88b1a2687fc3ff1e3b62ecc670560c5c6fef8d2f', 'user_id': 2, 'email': 'tony@gmail.com'}
# url = 'http://127.0.0.1:8000/api/actor/'
# # url = 'http://127.0.0.1:8000/api/user/auth-token/'

# payload = {'client_id': 'T0LkP3v4vKiwGDYWFP0ihfHUyf5E6GSqs0IGuxUS', 'client_secret':'pbkdf2_sha256$260000$3VD4PEwI7wfgYFwX0l6SlX$nHpnXLf7IMEorvgQXk7TVuLAOnceWUaznzlwgzRsirY', '​grant_type':'​password', 'username':'petertalk@gmail.com', 'password':'propensity'}
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Token 88b1a2687fc3ff1e3b62ecc670560c5c6fef8d2f'
# }
# r = requests.get(url, data=payload, headers=headers)

# print(r.json())

# import requests

url = "http://127.0.0.1:8000/oauth/token/"

payload = {
    "client_id": r"T0LkP3v4vKiwGDYWFP0ihfHUyf5E6GSqs0IGuxUS",
    "client_secret": r"pbkdf2_sha256$260000$3VD4PEwI7wfgYFwX0l6SlX$nHpnXLf7IMEorvgQXk7TVuLAOnceWUaznzlwgzRsirY=",
    "grant_type": r"password",
    "username": r"talk2peteresezobor@gmail.com",
    "password": r"propensity"
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.json())