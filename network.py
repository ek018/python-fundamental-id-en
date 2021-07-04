import requests

url: str = 'https://detik.com'

try:
    response = requests.get(url)
    print(response.status_code)
    print(response.text)
except Exception as e:
    print(f'Error get data {e}')
