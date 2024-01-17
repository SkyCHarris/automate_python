import requests

r = requests.get('https://httbin.org/delay/6', timeout=3)

print(r)