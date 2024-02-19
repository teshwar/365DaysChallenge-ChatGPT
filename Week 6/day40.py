"""
Day 40: Handling Forms and Sessions

    Explore techniques for interacting with forms on websites.
    Learn how to maintain sessions during web scraping.
"""

import requests

def main():
    try:
        # Specify the URL to request (replace 'youtube.com' with the actual hostname causing the error)
        url = 'https://youtube.com'
        
        # Perform an HTTP GET request
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print('Request successful!')
            print('Response content:', response.text)
        else:
            print(f'Request failed with status code {response.status_code}')
    except Exception as e:
        print('An error occurred:', e)

if __name__ == "__main__":
    main()
