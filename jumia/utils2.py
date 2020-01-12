"""
    name='utils',
    project='jumia'
    date='1/11/2020',
    author='Oshodi Kolapo',
"""
import csv

products_list = []
percents_list = []
prices_list = []
old_prices_list = []
img_urls_list = []
product_urls_list = []


def number_of():
    return len(prices_list)


with open('iphone.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        percents_list.append(row[0])
        products_list.append(row[1])
        prices_list.append(row[2])
        old_prices_list.append(row[3])
        img_urls_list.append(row[4])
        product_urls_list.append(row[5])
