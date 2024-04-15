import requests
from bs4 import BeautifulSoup
import json

url ="https://www.bbc.com/portuguese"

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

# Convertendo para JSON
links_json = json.dumps(links)

print(links_json)
