import sys
import random
import requests
from urllib.parse import urljoin
from html.parser import HTMLParser
from spydr.configs import USER_AGENTS
from spydr.helper import sanitize, get_domain, is_valid, contain_static


class SpydrParser(HTMLParser):
    """
        HTML Parser to fetch URLs and show assets
    """
    def handle_starttag(self, tag, attrs):
        for key, val in attrs:
            if key == "href":
                if contain_static(val):
                    pass
                elif tag == "a":
                    url = urljoin(self.url, val)
                    url = sanitize(url)
                    if is_valid(url, self.domain):
                        self.urls.append(url)

                else:
                    pass
    
    def run(self, url):
        self.url = url
        self.domain = get_domain(url)
        self.urls = []

        try:
            response = requests.get(url, headers={'user-agent': random.choices(USER_AGENTS)[0]})
            html = response.text
            self.feed(html)
        except KeyboardInterrupt:
            print("You stopped the Process.. Exiting now! .\n.\n.")
            sys.exit(1)
        except Exception as ex:
            print(f"Unexpected error {ex} occured.. Exiting now! .\n.\n.")
            sys.exit(1)
        
        return self.urls


class Spydr:
    def __init__(self):
        self.to_visit = []
        self.visited = set([])
        self.parser = SpydrParser()

    def crawl(self,target_url):
        target_url = sanitize(target_url)
        self.to_visit.append(target_url)
        try:
            while len(self.to_visit) > 0:
                url = self.to_visit.pop(0)
                print(f"Spydr now visiting: {url}")
                urls = self.parser.run(url)
                self.visited.add(url)
                for url in urls:
                    if url not in self.visited and url not in self.to_visit:
                        self.to_visit.append(url)
        except Exception as ex:
            print(f"Error Occured: {ex}")
            pass
        finally:
            print(f"Spydr finished crawling at: {target_url}")
            return self.visited