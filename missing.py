import requests
from bs4 import BeautifulSoup
import os
import time
from PIL import Image
from io import BytesIO

def download_image(url, filename, retries=5):
    filepath = os.path.join(download_folder, filename)
    if os.path.exists(filepath):
        print(f"Filename {filename} already exists, download canceled")
        return
    
    attempt = 0
    while attempt < retries:
        try:
            print(f"Downloading {filename}")
            response = requests.get(url)
            img_data = response.content

            try:
                img = Image.open(BytesIO(img_data))
                img.verify()
            except (IOError, SyntaxError) as e:
                print(f"Filename {filename} corrupt, download canceled")
                return
            
            os.makedirs(download_folder, exist_ok=True)
            with open(filepath, 'wb') as handler:
                handler.write(img_data)
            print(f"Filename {filename} downloaded")
            return
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"Download of {filename} failed, retry {e}")
            if attempt < retries:
                print(f"Retrying in 60 seconds... (Attempt {attempt}/{retries})")
                time.sleep(60)
            else:
                print(f"Download failed after {retries} attempts.")
                return

def format_subpage_number(sub_page):
    return f"{sub_page:02d}"

def get_total_subpages(soup):
    subpage_info = soup.find(text=lambda text: text and "Sous-page" in text)
    if subpage_info:
        total_subpages = int(subpage_info.split('/')[-1])
        return total_subpages
    return 1

def scrape_page(timestamp, page, sub_page):
    base_url = f"http://web.archive.org/web/{timestamp}000000/http://www.rtbf.be/services/teletexte/cgi-bin/GetPage.cgi"
    
    page = int(page)
    sub_page = int(sub_page)
    
    formatted_subpage = format_subpage_number(sub_page)
    filename = f"{timestamp}_{page}_{formatted_subpage}.gif"
    
    if os.path.exists(os.path.join(download_folder, filename)):
        print(f"Filename {filename} already exists, skipping.")
        return
    
    sub_page_url = f"{base_url}?PAGE={page}&SUB={sub_page}"
    print(f"Fetching sub-page: {sub_page_url}")

    try:
        response = requests.get(sub_page_url, allow_redirects=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tag = soup.find('img')
            if img_tag:
                img_url = img_tag['src']
                if "page" in img_url and img_url.endswith(".gif"):
                    full_img_url = f"http://web.archive.org{img_url}"
                    print(f"Downloading image from: {full_img_url}")
                    download_image(full_img_url, filename)
                else:
                    print("No valid image found or link is incorrect.")
            else:
                print("No image found on the sub-page.")
        else:
            print(f"HTTP error {response.status_code} for the sub-page {sub_page}")
    except Exception as e:
        print(f"Error fetching page {page}, sub-page {sub_page}: {e}")
    
    time.sleep(30)

if __name__ == "__main__":
    download_folder = 'teletexte_images'
    
    with open('id.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split()

        if len(parts) != 3:
            print(f"Invalid line format: {line}. Skipping.")
            continue

        timestamp, page, sub_page = parts

        if len(timestamp) != 8 or not timestamp.isdigit():
            print(f"Invalid timestamp format: {timestamp}. Skipping.")
            continue

        scrape_page(timestamp, page, sub_page)

