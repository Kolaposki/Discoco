from django.db import IntegrityError, OperationalError
from django.shortcuts import render

from jumia import utils, utils2
from .models import IphoneScrape, AndroidScrape


# Create your views here.

def index(request):
    return render(request, 'home.html')


def jumia_home(request):
    return render(request, 'jumia.html')


def android_scrape(request):
    percent = utils.percents_list
    product = utils.products_list
    price = utils.prices_list
    old_price = utils.old_prices_list
    product_url = utils.product_urls_list
    img_url = utils.img_urls_list

    try:
        AndroidScrape.objects.all().delete()
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(utils.number_of()):
            details = AndroidScrape(product=product[count], percent=percent[count], price=price[count],
                                    old_price=old_price[count],
                                    product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("products Saved to database")
    all_details = AndroidScrape.objects.all()
    total_products = utils.number_of()

    return render(request, 'android.html', {"scrapes": all_details, "total": total_products})


def iphone_scrape(request):
    percent = utils2.percents_list
    product = utils2.products_list
    price = utils2.prices_list
    old_price = utils2.old_prices_list
    product_url = utils2.product_urls_list
    img_url = utils2.img_urls_list

    try:
        IphoneScrape.objects.all().delete()
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(utils2.number_of()):
            details = IphoneScrape(product=product[count], percent=percent[count], price=price[count],
                                   old_price=old_price[count],
                                   product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("products Saved to database")
    all_details = IphoneScrape.objects.all()
    total_products = utils2.number_of()
    return render(request, 'iphone.html', {"scrapes": all_details, "total": total_products})
