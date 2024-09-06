import requests
from bs4 import BeautifulSoup
import os
import time
from PIL import Image
from io import BytesIO
import argparse

def download_image(url, filename, retries=5):
    filepath = os.path.join(download_folder, filename)
    if os.path.exists(filepath):
        print(f"Filename {filename} already exist, download canceled")
        return
    
    attempt = 0
    while attempt < retries:
        try:
            print(f"Download {filename}")
            response = requests.get(url)
            img_data = response.content

            try:
                img = Image.open(BytesIO(img_data))
                img.verify()  # Check picture
            except (IOError, SyntaxError) as e:
                print(f"Filename {filename} corupt, download canceled")
                return
            
            os.makedirs(download_folder, exist_ok=True)  # Create folder
            with open(filepath, 'wb') as handler:
                handler.write(img_data)
            print(f"Filename {filename} downloaded")
            return  # Stop loop if download ok
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"Download of {filename} failed, new try {e}")
            if attempt < retries:
                print(f"New try in 60 secondes... (Try {attempt}/{retries})")
                time.sleep(60)  # Wait
            else:
                print(f"Download failed after {retries} try.")
                return

def format_subpage_number(sub_page):
    return f"{sub_page:02d}"

def get_total_subpages(soup):
    subpage_info = soup.find(text=lambda text: text and "Sous-page" in text)
    if subpage_info:
        total_subpages = int(subpage_info.split('/')[-1])
        return total_subpages
    return 1

# Master
def scrape_pages(pages, timestamp):
    base_url = f"http://web.archive.org/web/{timestamp}000000/http://www.rtbf.be/services/teletexte/cgi-bin/GetPage.cgi"

    for page in pages:
        sub_page_url = f"{base_url}?PAGE={page}&SUB=1"
        print(f"Fetching: {sub_page_url}")

        try:
            response = requests.get(sub_page_url, allow_redirects=True)
            if response.status_code == 200:
                redirected_url = response.url
                print(f"Redirection to: {redirected_url}")

                redirected_timestamp = redirected_url.split('/')[4][:8]

                soup = BeautifulSoup(response.text, 'html.parser')
                total_subpages = get_total_subpages(soup)
                print(f"Nbr total subpage for the page {page}: {total_subpages}")

                for sub_page in range(1, total_subpages + 1):
                    formatted_subpage = format_subpage_number(sub_page)
                    filename = f"{redirected_timestamp}_{page}_{formatted_subpage}.gif"
                    
                    if os.path.exists(os.path.join(download_folder, filename)):
                        print(f"Filename {filename} already exist, go to the next subpage.")
                        continue

                    sub_page_url = f"{base_url}?PAGE={page}&SUB={sub_page}"
                    print(f"Fetching sub-page: {sub_page_url}")

                    sub_response = requests.get(sub_page_url, allow_redirects=True)
                    if sub_response.status_code == 200:
                        sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                        img_tag = sub_soup.find('img')
                        if img_tag:
                            img_url = img_tag['src']
                            if "page" in img_url and img_url.endswith(".gif"):
                                full_img_url = f"http://web.archive.org{img_url}"
                                print(f"Download picture from: {full_img_url}")
                                download_image(full_img_url, filename)
                            else:
                                print(f"No picture found or the link is wrong")
                        else:
                            print(f"No picture found on the subpage")
                    else:
                        print(f"Oops http error {sub_response.status_code} for the subpage {sub_page}")
                    time.sleep(30)  # wait
            else:
                print(f"Oops http error {response.status_code} for the page {page}")

        except Exception as e:
            print(f"Oops error on the page {page}: {e}")

        time.sleep(60)  # wait

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape RTBF teletexte pages from Wayback Machine.")
    parser.add_argument("timestamp", type=str, help="Timestamp in the format YYYYMMDD (e.g., 20030419).")
    args = parser.parse_args()

    if len(args.timestamp) != 8 or not args.timestamp.isdigit():
        print("The timestamp need to be in the format YYYYMMDD (e.g., 20030419).")
        exit(1)

    download_folder = 'teletexte_images'

    pages = range(100, 1000)

    scrape_pages(pages, args.timestamp)
