import requests
import json

# url = 'http://127.0.0.1:8000/users/change-password/'
# url = 'http://127.0.0.1:8000/users/password_reset/confirm/'
url = "http://127.0.0.1:8000/api/videos/1/likes/"

payload = {'user_id': 1, 'video_id': 1}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token afbf91b454b50cc56637d34b77133fef3c6604da'
}
r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.json())