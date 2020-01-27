from django.db import IntegrityError, OperationalError, connection
from django.shortcuts import render

from jumia import utils
from .models import *


def index(request):
    return render(request, 'home.html')


def jumia_home(request):
    return render(request, 'jumia.html')


def android_scrape(request, discount=50):
    if not discount or discount > 99 or discount < 5 or discount is None or discount is any(['', ' ', ]):
        discount = 50

    base_url = 'https://www.jumia.com.ng/android-phones/?page='
    percent, product, price, old_price, product_url, img_url = utils.scrape_data(discount, product_type_url=base_url)
    number_of_products = len(product)

    try:
        AndroidScrape.objects.all().delete()
        print("Deleted old Android products from database")
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(number_of_products):
            details = AndroidScrape(product=product[count], percent=percent[count], price=price[count],
                                    old_price=old_price[count],
                                    product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("New Android products saved to database")
    all_details = AndroidScrape.objects.all()
    total_products = number_of_products

    return render(request, 'android.html', {"scrapes": all_details, "total": total_products, "discount_per": discount})


def iphone_scrape(request, discount=50):
    if not discount or discount > 99 or discount < 5 or discount is None or discount is any(['', ' ', ]):
        discount = 50

    base_url = 'https://www.jumia.com.ng/ios-phones/?page='
    percent, product, price, old_price, product_url, img_url = utils.scrape_data(discount, product_type_url=base_url)
    number_of_products = len(product)

    try:
        IphoneScrape.objects.all().delete()
        print("Deleted old Iphone products from database")
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(number_of_products):
            details = IphoneScrape(product=product[count], percent=percent[count], price=price[count],
                                   old_price=old_price[count],
                                   product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("New Iphone products saved to database")
    all_details = IphoneScrape.objects.all()
    total_products = number_of_products

    return render(request, 'iphone.html', {"scrapes": all_details, "total": total_products, "discount_per": discount})


def computing_scrape(request, discount=50):
    if not discount or discount > 99 or discount < 5 or discount is None or discount is any(['', ' ', ]):
        discount = 50

    base_url = 'https://www.jumia.com.ng/computing/?page='
    percent, product, price, old_price, product_url, img_url = utils.scrape_data(discount, product_type_url=base_url)
    number_of_products = len(product)

    try:
        ComputingScrape.objects.all().delete()
        print("Deleted old Computing products from database")
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(number_of_products):
            details = ComputingScrape(product=product[count], percent=percent[count], price=price[count],
                                      old_price=old_price[count],
                                      product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("New Computing products saved to database")
    all_details = ComputingScrape.objects.all()
    total_products = number_of_products

    return render(request, 'computing.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def electronics_scrape(request, discount=50):
    if not discount or discount > 99 or discount < 5 or discount is None or discount is any(['', ' ', ]):
        discount = 50

    base_url = 'https://www.jumia.com.ng/electronics/?page='
    percent, product, price, old_price, product_url, img_url = utils.scrape_data(discount, product_type_url=base_url)
    number_of_products = len(product)

    try:
        ElectronicsScrape.objects.all().delete()
        print("Deleted old Electronics products from database")
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(number_of_products):
            details = ElectronicsScrape(product=product[count], percent=percent[count], price=price[count],
                                        old_price=old_price[count],
                                        product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("New Electronics products saved to database")
    all_details = ElectronicsScrape.objects.all()
    total_products = number_of_products

    return render(request, 'electronics.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def fashion_scrape(request, discount=50):
    if not discount or discount > 99 or discount < 5 or discount is None or discount is any(['', ' ', ]):
        discount = 50

    base_url = 'https://www.jumia.com.ng/category-fashion-by-jumia/?page='
    percent, product, price, old_price, product_url, img_url = utils.scrape_data(discount, product_type_url=base_url)
    number_of_products = len(product)

    try:
        FashionScrape.objects.all().delete()
        print("Deleted old Fashion products from database")
    except OperationalError:
        pass

    count = 0
    try:
        for item in range(number_of_products):
            details = FashionScrape(product=product[count], percent=percent[count], price=price[count],
                                    old_price=old_price[count],
                                    product_url=product_url[count], img_url=img_url[count])
            details.save()
            count += 1
    except IntegrityError:
        pass

    print("New Fashion products saved to database")
    all_details = FashionScrape.objects.all()
    total_products = number_of_products

    return render(request, 'fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})
