import requests
from bs4 import BeautifulSoup


base_url = 'https://gitlab.com/explore/projects/topics/python?non_archived=true&page={}&sort=name_asc&topic=python'

page = 1

next_exists = True

while next_exists:
    url = base_url.format(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    if soup.find("li", {"class": "page-item next"}) is not None:
        page += 1
    else:
        next_exists = False

print(page)

