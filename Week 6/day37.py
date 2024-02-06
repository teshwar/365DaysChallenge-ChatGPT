"""
Day 37: HTML Parsing with BeautifulSoup

    Explore HTML parsing with BeautifulSoup.
    Extract specific information from the HTML content.
"""

from bs4 import BeautifulSoup

# Sample HTML content to parse
html_content = """
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome to BeautifulSoup</h1>
    <p>This is a sample paragraph.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    <a href="https://www.example.com">Visit Example</a>
</body>
</html>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract specific information from the HTML content
heading = soup.find('h1')  # Find the <h1> tag
paragraph = soup.find('p')  # Find the <p> tag
list_items = soup.find_all('li')  # Find all <li> tags
link = soup.find('a')  # Find the <a> tag

# Print the extracted information
print("Heading:", heading.text)
print("Paragraph:", paragraph.text)
print("List Items:")
for item in list_items:
    print("-", item.text)
print("Link:", link['href'])
