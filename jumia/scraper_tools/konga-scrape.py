"""
    name='konga-scrape',
    project='discoco'
    date='2/14/2020',
    author='Oshodi Kolapo',
"""
from bs4 import BeautifulSoup
import requests as req

url = 'https://www.konga.com/category/konga-fashion-1259'
reqs = req.get(url)
content = reqs.content
soup = BeautifulSoup(content, "lxml", from_encoding="utf-8")

discount_tag = soup.find("span", {"class": "_4472a_zYlL- _6c244_q2qap"})

print(discount_tag)
