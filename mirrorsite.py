import requests
from bs4 import BeautifulSoup
import os
import shutil
import urllib.parse

def mirror_website(source_url, target_url):
    """
    Crawls the source website and mirrors it to the target URL.
    
    Args:
        source_url (str): The URL of the website to be crawled.
        target_url (str): The URL where the mirrored website will be hosted.
    """
    
    # Create a directory to store the mirrored website
    target_dir = os.path.join(os.getcwd(), 'mirrored_website')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Fetch the HTML content of the source website
    response = requests.get(source_url)
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Update the URLs in the HTML content to point to the target URL
    for tag in soup.find_all(['a', 'img', 'link', 'script']):
        if 'src' in tag.attrs:
            tag['src'] = urllib.parse.urljoin(target_url, tag['src'])
        if 'href' in tag.attrs:
            tag['href'] = urllib.parse.urljoin(target_url, tag['href'])
    
    # Save the updated HTML content to a file in the target directory
    with open(os.path.join(target_dir, 'index.html'), 'wb') as f:
        f.write(soup.prettify().encode())
    
    # Copy any static assets (images, CSS, JS) to the target directory
    for tag in soup.find_all(['img', 'link', 'script']):
        if 'src' in tag.attrs:
            src_url = urllib.parse.urljoin(source_url, tag['src'])
            dst_path = os.path.join(target_dir, os.path.basename(tag['src']))
            
            # Download the asset and save it to the target directory
            response = requests.get(src_url, stream=True)
            with open(dst_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
    
    print(f'Website mirrored successfully to {target_url}')

# Example usage
mirror_website('https://imagetwistcams.com', 'https://bkgb.github.io')
