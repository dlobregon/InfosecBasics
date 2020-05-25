# implement a function that given a URL, parses it and returns a tuple with its protocol, domain, and path.
# for example, for "https://www.google.com/seach", it would retunr ("https", "www.google.com","/search")

# imports go here
from urllib.parse import urlparse

def parse_url(url):
    operationResult= urlparse(url)
    return ( operationResult.scheme, operationResult.netloc, operationResult.path)

print(parse_url("https://www.google.com/search"))