import urllib.request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_title = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.is_title = True

    def handle_data(self, data):
        if self.is_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.is_title = False


def fetch_title(url):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode('utf-8')
    parser = MyHTMLParser()
    parser.feed(webContent)
    return parser.title


# Fetch and print the title of a webpage
url = "http://example.com"
print(f"Title of the webpage: {fetch_title(url)}")