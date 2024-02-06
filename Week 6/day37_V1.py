"""
Day 37: HTML Parsing with BeautifulSoup

    Explore HTML parsing with BeautifulSoup.
    Extract specific information from the HTML content.

    This one from external website where you print all the links
"""

import requests
from bs4 import BeautifulSoup

def fetch_html_content(url):
    try:
        # Send a GET request to the URL to fetch the HTML content
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the HTML content
            return response.text
        else:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_html_content(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find specific elements and extract information
    # Example: Find the title of the webpage
    title = soup.find('title')
    if title:
        print("Title:", title.text.strip())
    else:
        print("Title not found.")

    # Example: Find all links (<a> tags) on the webpage
    links = soup.find_all('a')
    print("Links:")
    for link in links:
        print("-", link.get('href'))

if __name__ == "__main__":
    # URL of the website to scrape
    target_url = 'https://pypi.org/project/beautifulsoup4/'

    # Fetch HTML content from the website
    html_content = fetch_html_content(target_url)
    if html_content:
        # Parse HTML content and extract information
        parse_html_content(html_content)
