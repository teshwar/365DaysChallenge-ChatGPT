"""
Day 38: Advanced HTML Parsing

    Learn advanced techniques for parsing complex HTML structures.
    Handle scenarios involving nested elements and attributes.
"""

from bs4 import BeautifulSoup

# Sample HTML content with nested elements and attributes
html_content = """
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <div id="main-content">
        <h1>Welcome to BeautifulSoup</h1>
        <p>This is a sample paragraph.</p>
        <ul class="item-list">
            <li><a href="https://www.example.com/page1">Page 1</a></li>
            <li><a href="https://www.example.com/page2">Page 2</a></li>
            <li><a href="https://www.example.com/page3">Page 3</a></li>
        </ul>
    </div>
</body>
</html>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting information from nested elements and attributes
# Example: Find the text content of the <h1> tag within the <div> with id "main-content"
main_div = soup.find('div', id='main-content')
if main_div:
    heading = main_div.find('h1')
    if heading:
        print("Heading:", heading.text)
    else:
        print("Heading not found.")

# Example: Find all links (<a> tags) within the <ul> with class "item-list"
item_list = soup.find('ul', class_='item-list')
if item_list:
    print("Links:")
    links = item_list.find_all('a')
    for link in links:
        print("-", link['href'])
else:
    print("List not found.")
