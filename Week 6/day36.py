"""
Day 36: Introduction to Web Scraping

    Learn the basics of web scraping.
    Use the requests library to fetch HTML content from a webpage.
"""

import requests

def fetch_webpage(url):
    try:
        # Send a GET request to the URL to fetch the HTML content
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the HTML content of the webpage
            print(response.text)
        else:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL of the webpage to scrape
    target_url = 'https://youtube.com'

    # Call the function to fetch the webpage
    fetch_webpage(target_url)
