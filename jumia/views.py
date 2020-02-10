from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'home.html')


def jumia_home(request):
    return render(request, 'jumia.html')


def android_scrape(request, discount=50):
    all_details = AndroidScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'android.html', {"scrapes": all_details, "total": total_products, "discount_per": discount})


def iphone_scrape(request, discount=50):
    all_details = IphoneScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'iphone.html', {"scrapes": all_details, "total": total_products, "discount_per": discount})


def computing_scrape(request, discount=50):
    all_details = ComputingScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'computing.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def electronics_scrape(request, discount=50):
    all_details = ElectronicsScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'electronics.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def fashion_scrape(request, discount=50):
    all_details = FashionScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def health_beauty_scrape(request, discount=50):
    all_details = HealthBeautyScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'health-beauty.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def men_fashion_scrape(request, discount=50):
    all_details = MenFashionScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'men-fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def women_fashion_scrape(request, discount=50):
    all_details = WomenFashionScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'women-fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def kids_fashion_scrape(request, discount=50):
    all_details = KidsFashionScrape.objects.filter(percent__gte=discount)
    total_products = len(all_details)
    return render(request, 'kids-fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})
