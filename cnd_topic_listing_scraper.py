import requests
from bs4 import BeautifulSoup
import csv
import cnd_page_with_video_scraper as CndPage

# URL to scrape
url = 'https://student.craigndave.org/videos/aqa-8525-slr2-memory-and-storage'

# Send GET request
response = requests.get(url)

products = []  # List to store product names and URLs

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Assuming product names and URLs are in `a` tags with a class `product-name`
    # You need to update this part based on the actual HTML structure
    
    product_containers = soup.find_all('div', class_='archive-listing')
    
    for container in product_containers:
        
        #products.append([container])

        title = container.a.text
        url = container.a.get('href') 
            
        video_code = "https://www.youtube.com/watch?v={}".format(CndPage.extract_video_url_from_target_page(url))

        products.append([title, video_code])
        # .get('href')  # Get the href attribute
        
        # product-name
        # products.append([product_name, product_url])  # Add to our list
    
    # Write to CSV f'data/{output_filename}.csv'
    with open('data/products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'URL'])  # Write the header
        writer.writerows(products)  # Write product data
else:
    print('Failed to retrieve the webpage')

