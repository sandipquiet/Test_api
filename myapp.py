import requests

URL = 'http://127.0.0.1:8000/studen_info/1'

r = requests.get(url = URL)

data = r.json()

print(data)
