import requests
from bs4 import BeautifulSoup

url: str = 'https://detik.com'

try:
    response = requests.get(url)
    print(response.status_code)
    # print(response.text)
    soup = BeautifulSoup(response.text, features="html.parser")
    print(soup.title.string)
except Exception as e:
    print(f'Error get data {e}')


