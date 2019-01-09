import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
header = {'user-agent':ua.chrome}
s = requests.Session()
s.proxies = {'http': 'http://10.121.11.32'}
google_page = s.get('https://www.google.com', headers=header)

soup = BeautifulSoup(google_page.content, 'lxml')

print(soup.prettify())

# Identify some Tags