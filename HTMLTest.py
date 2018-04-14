from urllib.parse import urlparse

from lxml.html import parse
from lxml.html import urljoin
import pathlib

home_page = "C:\ggtemp\STDF_Dictionary_Technical 201803\Home\Home.html"

parsed = parse(home_page)

doc = parsed.getroot()
print(doc.base_url)
print(pathlib.Path(doc.base_url).as_uri())
for a_link in doc.findall('.//a'):
    print(a_link.get('href'))
    print(a_link.text_content())

print(doc.findall('.//a')[1].get('href'))
abs_url = urljoin(doc.base_url, doc.findall('.//a')[1].get('href'))
print(abs_url)
parsed_1 = parse(abs_url)
doc_1 = parsed_1.getroot()


for a_link in doc_1.findall('.//a'):
    print(a_link.get('href'))
    print(a_link.text_content())
