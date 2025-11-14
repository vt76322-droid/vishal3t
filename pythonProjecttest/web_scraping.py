import urllib.request
from bs4 import BeautifulSoup

url = "http://example.com"  # Change this to the URL you want to scrape
response = urllib.request.urlopen(url)
webContent = response.read()

soup = BeautifulSoup(webContent, "html.parser")
print(soup.title.string)