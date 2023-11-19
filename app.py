import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse


# Function to download images
def download_image(url, folder_path):
    response = requests.get(url, stream=True)
    # Extract the file name from the URL and clean it
    file_name = os.path.join(folder_path, os.path.basename(urlparse(url).path))
    with open(file_name, 'wb') as out_file:
        for chunk in response.iter_content(1024):
            out_file.write(chunk)


# Function to extract images from a webpage
def extract_images(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')

    # Create a folder to save images
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Download and save images
    for img in img_tags:
        img_url = urljoin(url, img.get('src'))
        download_image(img_url, folder_path)


# Example usage
if __name__ == "__main__":
    # URL of the website to scrape
    website_url = 'https://watchcp.co/'
    # Folder where images will be saved
    download_folder = 'downloaded_images'
    extract_images(website_url, download_folder)
