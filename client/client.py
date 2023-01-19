import requests

# url = 'http://127.0.0.1:8000/users/password_reset/'
url = 'http://127.0.0.1:8000/users/password_reset/?token=d5210d82014c3e899669a743c2'


payload = {'email': 'james@gmail.com'}
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': ''
# }
r = requests.get(url)

if r.status_code == 200:
    print(r.json())