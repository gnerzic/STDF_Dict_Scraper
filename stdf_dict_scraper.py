# this script will scrape the STDF dictionary to output it into an
# easy to use EXCEL worksheet.
# REMEMBER:
#  run "python -m http.server" on the command line at the root of the dictionary

from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

home_url = "http://localhost:8000/home/home.html"


def main():
    # try to open the dictionaries home page. if it doesn't work stop with error
    try:
        home_page_request = requests.get(home_url)
        # parse the page with BeautifulSoup
        home_soup = BeautifulSoup(home_page_request.content, 'lxml')

        # process the content page
        # the links in the page are local urls, so need to be made absolute
        # urls using urljoin
        # the link in the page use non-htlm slashes which need to be replaced
        # finally the url is made lowercase before loading it.
        parse_stdf_dict(urljoin(home_page_request.url, home_soup("a")[1]['href']
                                .replace("\\", "/").lower()))
    except:
        print('ERROR: Could not connect to dictionary home page.')
        print("url:", home_url)
        print("please ensure run \"python -m http.server\" on the command "
              "line at the root of the dictionary")
        raise


def parse_stdf_dict(content_page_url):
    # request page
    content_page_request = requests.get(content_page_url)
    # parse the page with BeautifulSoup
    content_soup = BeautifulSoup(content_page_request.content, 'lxml')

    # for each anchor link on the page
    for content_link in content_soup("a"):
        # ignore breadcrumb links
        if not content_link.parent.has_attr('id') \
                or content_link.parent['id'] != "breadcrumbs" :
            content_link_url = urljoin(content_page_url, content_link['href']
                                       .replace("\\", "/")).lower()

            # based on the type of link call a different function by
            # - contruct a string that represents the function call
            # - invoke the function call using python's eval function
            function_name = "parse_" + content_link.text.lower()+"(\""+content_link_url+"\")"
            eval(function_name)


def parse_templates(templates_page_url):
    print("parse_templates:", templates_page_url)


def parse_enumerations(enumerations_page_url):
    print("parse_enumerations:", enumerations_page_url)


def parse_definitions(definitions_page_url):
    print("parse_definitions:", definitions_page_url)


def parse_patterns(patterns_page_url):
    print("parse_patterns:", patterns_page_url)


def parse_dimensions(dimensions_page_url):
    print("parse_dimensions:", dimensions_page_url)


def parse_rules(rules_page_url):
    print("parse_rules:", rules_page_url)


def parse_reconciliations(reconciliations_page_url):
    print("parse_reconciliations:", reconciliations_page_url)


main()