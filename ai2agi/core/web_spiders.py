import requests
from bs4 import BeautifulSoup
import json

class WebSpider:
    def __init__(self, base_url):
        """
        Initialize the WebSpider with a base URL to start the scraping process.

        :param base_url: The URL to begin scraping data from.
        """
        self.base_url = base_url  # The base URL to start scraping
        self.visited_urls = set()  # Set to store URLs that have been visited to avoid repetition
        self.data = []  # List to store scraped data

    def fetch_page(self, url):
        """
        Fetch the HTML content of a webpage using requests.

        :param url: The URL of the page to fetch.
        :return: The HTML content of the page or None if the page couldn't be fetched.
        """
        try:
            print(f"Fetching page: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch page: {url}, Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error fetching page {url}: {e}")
            return None

    def parse_html(self, html):
        """
        Parse the HTML content using BeautifulSoup to extract relevant information.

        :param html: The HTML content of the page.
        :return: A dictionary containing the parsed data.
        """
        soup = BeautifulSoup(html, 'html.parser')
        # Example of extracting title and description, you can customize this to your needs
        title = soup.title.string if soup.title else "No title"
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else "No description"

        parsed_data = {
            "title": title,
            "description": description_content,
            "url": soup.base.get('href', self.base_url)  # Get the base URL from the page
        }
        
        return parsed_data

    def crawl(self, url, depth=2):
        """
        Crawl through the pages starting from the given URL.

        :param url: The URL to start scraping.
        :param depth: The depth of the crawl (how many levels deep you want to go).
        """
        if depth == 0 or url in self.visited_urls:
            return  # Stop if depth is 0 or URL has already been visited
        
        print(f"Visiting: {url}")
        self.visited_urls.add(url)  # Mark this URL as visited

        html = self.fetch_page(url)
        if html:
            data = self.parse_html(html)
            self.data.append(data)  # Store the extracted data

            # Find all the links in the page and recursively visit them
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', href=True)

            for link in links:
                next_url = link['href']
                # If the link is an absolute URL, visit it directly
                if next_url.startswith('http'):
                    self.crawl(next_url, depth-1)
                else:
                    # Otherwise, join the base URL with the relative URL
                    self.crawl(self.base_url + next_url, depth-1)

    def save_data(self, filename='scraped_data.json'):
        """
        Save the scraped data to a JSON file.

        :param filename: The name of the file where the data will be saved.
        """
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"Data saved to {filename}")

# Example usage of WebSpider
if __name__ == "__main__":
    base_url = "https://example.com"  # Replace this with the URL you want to scrape
    spider = WebSpider(base_url)
    
    # Start crawling from the base URL, set depth to 2 (you can increase/decrease this)
    spider.crawl(base_url, depth=2)
    
    # Save the scraped data to a JSON file
    spider.save_data("scraped_data.json")
