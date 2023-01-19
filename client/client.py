import requests
import json

url = 'http://127.0.0.1:8000/users/change-password/'
# url = 'http://127.0.0.1:8000/users/password_reset/confirm/'


payload = {'old_password': 'petertalk', 'new_password': 'propensity'}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token afbf91b454b50cc56637d34b77133fef3c6604da'
}
r = requests.put(url, data=json.dumps(payload), headers=headers)

print(r.json())
# if r.status_code == 200:
#     print(r.json())
    