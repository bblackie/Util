import requests
from bs4 import BeautifulSoup
import csv
import re


'''
https://www.youtube-nocookie.com/embed/7Up7DIPkTzo?feature=oembed&iv_load_policy=1&modestbranding=1&rel=0&autohide=1&playsinline=1&autoplay=0
'''
def extract_video_url_from_target_page(url):

    # URL to scrape
    #url = 'https://student.craigndave.org/videos/ocr-gcse-j277-slr-1-1-von-neumann-architecture'

    # Send GET request
    response = requests.get(url)

    products = []  # List to store product names and URLs

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming product names and URLs are in `a` tags with a class `product-name`
        # You need to update this part based on the actual HTML structure
        
        container = soup.find('iframe')
        
        
            #products.append([container])
        # https://www.youtube-nocookie.com/embed/KBmoqwVt4Qg?list=PLCiOXwirraUCvYFmgaS_gQ4eKe1GJqIJa&iv_load_policy=1&modestbranding=1&rel=0&autohide=1&playsinline=1&autoplay=0,['https']


        src = container.get('src')
                
        # finding the file capture group 
        video_code = re.findall('https://www.youtube-nocookie.com/embed/([a-zA-Z0-9-_]+)', src)   
        
        print(video_code) 

        return video_code[0]
        #products.append([src, obj1])
            # .get('href')  # Get the href attribute
            
            # product-name
            # products.append([product_name, product_url])  # Add to our list
        
        # # Write to CSV f'data/{output_filename}.csv'
        # with open('data/video.csv', 'w', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(['Product Name', 'URL'])  # Write the header
        #     writer.writerows(products)  # Write product data
    else:
        print('Failed to retrieve the webpage')

