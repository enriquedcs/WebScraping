import requests
from fake_useragent import UserAgent

# Background on user-agents

ua = UserAgent()

header = {'user-agent':ua.chrome}

#print(ua.chrome)
s = requests.Session()
s.proxies = {'http': 'http://10.121.11.32'}
page = s.get('https://www.google.com', headers=header)
print(page.content)

# Background on Timeout

page = s.get('https://www.google.com', timeout=3)