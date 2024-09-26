import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return ' '.join([p.get_text() for p in soup.find_all('p')])