import re
from urllib.parse import urlparse


def sanitize(url):
    """
        Clean/Sanitize the URL:
            - URL should always start with "http://" or "https://"
            - Remove #
            - Remove last "/"
    """
    # Check if URL starts with HTTP, if not then add
    if url[0:4] != "http":
        url = "http://" + url

    # Check if URL contains #, if yes, remove it
    pound = url.find("#")
    if pound != -1:
        url = url[:pound]
    
    # Check if URL ends with "/", if yes, remove it
    l = len(url)
    if url[l-1] == "/":
        url = url[:l-1]

    # Return sanitized URL    
    return url

def get_domain(url):
    """
        Extract domain from given URL
            @input: given URL
            @output: domain of URL
    """
    parsed_url = urlparse(url)
    dom = parsed_url.netloc

    # Return domain extracted from URL
    return dom

def is_valid(url, domain):
    """
        Check if given, URL is valid
            - If the given URL matches the Regular Expression of valid URL, return True
            - else, return False
    """
    if re.match(r'^https?://([\w-]*\.)?' + domain + r'.*$', url, re.M|re.I):
        
        # Valid URL pattern
        return True
    else:
        # Invalid URL pattern
        return False

def contain_static(val): 
    """
        Check if URL is a static resource file
            - If URL pattern ends with 
    """   
    if re.match(r'^.*\.(jpg|jpeg|gif|png|css|js|ico|xml|rss|txt).*$', val, re.M|re.I):
        # Static file, return True
        return True
    else:
        # Not a static file, return False
        return False