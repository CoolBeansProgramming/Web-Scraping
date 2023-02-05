import requests
from bs4 import BeautifulSoup

# get URL
URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

print(page.text)