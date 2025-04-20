import os
import io
import hashlib
import requests
from PIL import Image
from duckduckgo_search import DDGS;

def download_image(url, folder_path):
    try:
        response = requests.get(url, timeout=5)
        image_content = response.content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        filename = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(filename, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ ERROR downloading {url} : {e}")

def scrape_duckduckgo_images(query, max_images=10, folder_path='./images'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print(f"🔍 Searching DuckDuckGo for '{query}' ...")
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=max_images)
        for result in results:
            download_image(result["image"], folder_path)


os.system('cls' if os.name == 'nt' else 'clear')
name = input("Enter your name: ")
num = int(input("Enter the number of images to download: "))
scrape_duckduckgo_images(name, max_images=num, folder_path="./anime_images")
