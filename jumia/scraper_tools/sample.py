"""
    name='sample',
    project='discoco'
    date='2/8/2020',
    author='Oshodi Kolapo',
"""
import schedule
from django.db import IntegrityError, OperationalError
import time
from bs4 import BeautifulSoup
import requests as req
import datetime

from jumia.models import *


def scrape_data(percent_range: int, product_type_url: str, product_category: str, db_name):
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
    print(f"\nStarted Scraping Process for {product_category} at {start_time}")
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
        db_name.objects.all().delete()
        print(f"Deleted old {product_category} products from database")
    except OperationalError:
        pass

    # Adding the new products
    number_of_products = len(products_list)
    count = 0
    try:
        for item in range(number_of_products):
            details = db_name(product=products_list[count], percent=percents_list[count],
                              price=prices_list[count],
                              old_price=old_prices_list[count],
                              product_url=product_urls_list[count], img_url=img_urls_list[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print(f"New {product_category} products saved to database")


# noinspection PyTypeChecker
def massive_scrape_job():
    start_time = datetime.datetime.now()
    print(f"Started MASSIVE SCRAPING JOB at {start_time}")

    # AndroidScrape
    scrape_data(50, 'https://www.jumia.com.ng/android-phones/?page=', product_category='Android',
                db_name=AndroidScrape)
    # IphoneScrape
    scrape_data(50, 'https://www.jumia.com.ng/ios-phones/?page=', product_category='IPhone',
                db_name=IphoneScrape)

    # ComputingScrape
    scrape_data(50, 'https://www.jumia.com.ng/computing/?page=', product_category='Computing',
                db_name=ComputingScrape)

    # ElectronicsScrape
    scrape_data(50, 'https://www.jumia.com.ng/electronics/?page=', product_category='Electronics',
                db_name=ElectronicsScrape)

    # FashionScrape
    scrape_data(50, 'https://www.jumia.com.ng/category-fashion-by-jumia/?page=', product_category='Fashion',
                db_name=FashionScrape)

    # HealthBeautyScrape
    scrape_data(50, 'https://www.jumia.com.ng/health-beauty/?page=', product_category='Health-Beauty',
                db_name=HealthBeautyScrape)

    # MenFashionScrape
    scrape_data(50, 'https://www.jumia.com.ng/mens-fashion/?page=', product_category='Men-Fashion',
                db_name=MenFashionScrape)

    # WomenFashionScrape
    scrape_data(50, 'https://www.jumia.com.ng/womens-fashion/?page=', product_category='Women-Fashion',
                db_name=WomenFashionScrape)

    # KidsFashionScrape
    scrape_data(50, 'https://www.jumia.com.ng/kids-fashion/?page', product_category='Kids-Fashion',
                db_name=KidsFashionScrape)

    print(f"Ended MASSIVE SCRAPING JOB at {datetime.datetime.now()}")
    print(f"Total time elapsed : {datetime.datetime.now() - start_time}")
