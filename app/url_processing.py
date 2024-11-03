
import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    # Add 'http://' if the URL does not start with 'http://' or 'https://'
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        # Send the GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from all <p> tags and join them into a single string
        paragraphs = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        return paragraphs if paragraphs else "No contents found on the page."
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors (invalid URL, timeouts, etc.)
        return f"Error fetching the URL: {e}"
