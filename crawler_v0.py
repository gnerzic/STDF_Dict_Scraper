from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests
# remember to run "python -m http.server" on the command line at the root of the dictionary
home = "http://localhost:8000/home/home.html"

r = requests.get(home)


soup = BeautifulSoup(r.content, "lxml")

links = soup('a')

print("Here")

print(r.url)
print(links[1]['href'].replace("\\", "/"))

follow_url = urljoin(r.url, links[1]['href'].replace("\\", "/"))
r1 = requests.get(follow_url)

soup1 = BeautifulSoup(r1.content, "lxml")

links1 = soup1('a')

print("There")