import requests
from bs4 import BeautifulSoup

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract headings
        headings = soup.find_all(['h1', 'h2', 'h3'])
        # Extract image URLs
        images = soup.find_all('img')
        print("Image URLs:")
        for image in images:
            image_url = image.get('src')  # Extract the 'src' attribute of the <img> tag
            if image_url:
                print(image_url)
            else:
                print("No 'src' attribute found for image tag:", image)

# Function to scrape data from multiple pages
def scrape_multiple_pages(base_url, num_pages):
    for page_num in range(1, num_pages + 1):
        # Construct the URL for each page
        page_url = f"{base_url}?page={page_num}"
        print("Scraping page:", page_url)
        # Call the function to scrape data from the current page
        scrape_page(page_url)

# Example usage
base_url = "https://unsplash.com/"
num_pages = 3  # Number of pages to scrape
scrape_multiple_pages(base_url, num_pages)
