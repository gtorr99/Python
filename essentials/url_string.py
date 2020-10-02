import re

def find_urls(string):
    url = re.findall(
            'http[s]?:\\/\\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),] \
                |(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
                string)
    return url

urls = find_urls("https://google.com dgdgdg hey...how are you? \
                 https://www.youtube.com")

print(urls)
        
