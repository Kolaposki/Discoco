"""
    name='utils',
    project='jumia'
    date='1/11/2020',
    author='Oshodi Kolapo',
"""
import random

from bs4 import BeautifulSoup
import requests as req

user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]


def scrape_data(percent_range: int, product_type_url: str):
    products_list = []
    percents_list = []
    prices_list = []
    old_prices_list = []
    img_urls_list = []
    product_urls_list = []

    def only_percent(mdata: str):
        try:
            return int(mdata.split()[0].replace('%', ''))
        except ValueError:
            return 0
        except IndexError:
            return 0

    print("\nStarted Scraping Process")
    count = 1
    base_url = product_type_url
    url = base_url + str(count)
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    while url and count < 6:
        reqs = req.get(url, headers=headers)
        content = reqs.content
        soup = BeautifulSoup(content, "lxml", from_encoding="utf-8")
        print(f"                            Scraping : {url}")

        main = soup.find_all("a", {"class": "link"})
        for page_index in main:
            percent_off = ''
            try:
                percent_off = page_index.find("span", {"class": "sale-flag-percent"}).text
            except AttributeError:
                pass

            percent = only_percent(percent_off)
            if percent < -percent_range:
                product = page_index.find("span", {"class": "name"}).text.replace('\uff1a', ':').replace('\uff09',
                                                                                                         ')').replace(
                    '\uff0c', ',').replace('\uff08', '(')
                price = page_index.find("span", {"class": "price"}).text.replace('\u20a6', '').strip()
                old_price = page_index.find("span", {"class": "price -old"}).text.replace('\u20a6', '').strip()
                img_url = page_index.find("img", attrs={'width': '220'}).attrs['data-src']
                product_url = page_index.get('href')

                percent = int(-1 * percent)

                percents_list.append(percent)
                prices_list.append(price)
                products_list.append(product)
                old_prices_list.append(old_price)
                img_urls_list.append(img_url)
                product_urls_list.append(product_url)

        count += 1
        url = base_url + str(count)

    print("Finished Scraping Process ):")
    return percents_list, products_list, prices_list, old_prices_list, product_urls_list, img_urls_list

