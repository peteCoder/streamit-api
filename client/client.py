import requests

url = 'http://127.0.0.1:8000/api/users/'

r = requests.get(url)

print(r.json())