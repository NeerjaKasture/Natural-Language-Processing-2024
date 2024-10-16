import requests
from bs4 import BeautifulSoup
import csv

# URL of the website you want to scrape
base_url = "https://thewireurdu.com/page/"
pages = 334

# Open the CSV file in write mode
with open('article_links.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header for the CSV file
    writer.writerow(['Link'])

    # Loop through the pages
    for page in range(1, pages + 1):
        # Send a GET request to fetch the HTML content of the page
        print(page)
        url = base_url + f"{page}"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            html_content = response.text  # Get the page content

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the main content area (adjusted class name as needed)
            main_content = soup.find('div', class_='main-post-list')

            if main_content:
                # Find all the sections with the class 'entry'
                div = main_content.findAll('section', class_='entry')

                # Extract the links
                for section in div:
                    content = section.find('h2', class_='posttitle')
                    if content:  # Check if content exists
                        anchor = content.find('a')
                        if anchor:  # Check if anchor exists
                            href = anchor['href']  # Extract the href attribute
                            writer.writerow([href])  # Write the link to the CSV file
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
