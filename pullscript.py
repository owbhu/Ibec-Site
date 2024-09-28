import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to get the HTML content of the website
def get_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.text

# Function to extract CSS and JS links from the HTML
def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    css_links = [urljoin(base_url, link.get('href')) for link in soup.find_all('link', rel='stylesheet')]
    js_links = [urljoin(base_url, script.get('src')) for script in soup.find_all('script') if script.get('src')]
    return css_links, js_links

# Function to download the content of the CSS and JS files
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Main function
def scrape_website(url):
    html = get_html(url)
    css_links, js_links = extract_links(html, url)
    
    print(f"HTML Content: \n{html[:1000]}...\n")
    
    # Downloading CSS files
    # for css_link in css_links:
    #     css_content = download_file(css_link)
    #     print(f"CSS Content from {css_link}:\n{css_content[:500]}...\n")
    
    # # Downloading JS files
    # for js_link in js_links:
    #     js_content = download_file(js_link)
    #     print(f"JavaScript Content from {js_link}:\n{js_content[:500]}...\n")

# Example usage
scrape_website('https://www.uoinvestmentgroup.org/')
