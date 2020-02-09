"""
    name='sample',
    project='discoco'
    date='2/8/2020',
    author='Oshodi Kolapo',
"""
import schedule
from django.db import IntegrityError, OperationalError
import time
from jumia.models import AndroidScrape
from bs4 import BeautifulSoup
import requests as req
import datetime


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

    start_time = datetime.datetime.now()
    print(f"Started Scraping Process at {start_time}")
    count = 1
    base_url = product_type_url
    url = base_url + str(count)
    while url and count < 11:
        reqs = req.get(url)
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

    print(f"Ended Scraping Process at {datetime.datetime.now()}")
    print(f"Time taken: {datetime.datetime.now() - start_time}")

    # Deleting the old products
    try:
        AndroidScrape.objects.all().delete()
        print("Deleted old Android products from database")
    except OperationalError:
        pass

    # Adding the new products
    number_of_products = len(products_list)
    count = 0
    try:
        for item in range(number_of_products):
            details = AndroidScrape(product=products_list[count], percent=percents_list[count],
                                    price=prices_list[count],
                                    old_price=old_prices_list[count],
                                    product_url=product_urls_list[count], img_url=img_urls_list[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("New Android products saved to database")

def job():
    print("I'm working...")

'''
# schedule.every(1).minutes.do(job)
schedule.every(29).minutes.do(scrape_data(70, 'https://www.jumia.com.ng/android-phones/?page='))
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''