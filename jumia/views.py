from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'home.html')


def jumia_home(request):
    percent = 65
    all_android_details = AndroidScrape.objects.filter(percent__gte=percent).order_by('-percent')[0:8]
    all_iphone_details = IphoneScrape.objects.filter(percent__gte=percent).order_by('-percent')[0:8]
    all_computing_details = ComputingScrape.objects.filter(percent__gte=percent).order_by('-percent')[0:8]
    all_electronics_details = ElectronicsScrape.objects.filter(percent__gte=percent).order_by('-percent')[0:8]
    all_menfashion_details = MenFashionScrape.objects.filter(percent__gte=percent).order_by('-percent')[0:8]
    all_womenfashion_details = WomenFashionScrape.objects.filter(percent__gte=percent).order_by('-percent')[0:8]

    return render(request, 'jumia.html',
                  {"scrapes1": all_android_details, "scrapes2": all_iphone_details, "scrapes3": all_computing_details,
                   "scrapes4": all_electronics_details, "scrapes5": all_menfashion_details,
                   "scrapes6": all_womenfashion_details})


def android_scrape(request, discount=50):
    all_details = AndroidScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)
    return render(request, 'android.html', {"scrapes": all_details, "total": total_products, "discount_per": discount})


def iphone_scrape(request, discount=50):
    all_details = IphoneScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)
    return render(request, 'iphone.html', {"scrapes": all_details, "total": total_products, "discount_per": discount})


def computing_scrape(request, discount=50):
    all_details = ComputingScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)
    return render(request, 'computing.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def electronics_scrape(request, discount=50):
    all_details = ElectronicsScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)
    return render(request, 'electronics.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def fashion_scrape(request, discount=50):
    all_details = FashionScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)
    return render(request, 'fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def health_beauty_scrape(request, discount=50):
    all_details = HealthBeautyScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)
    return render(request, 'health-beauty.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def men_fashion_scrape(request, discount=50):
    all_details = MenFashionScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_details, 16)

    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)

    return render(request, 'men-fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def women_fashion_scrape(request, discount=50):
    all_details = WomenFashionScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)

    paginator = Paginator(all_details, 16)
    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)

    return render(request, 'women-fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def kids_fashion_scrape(request, discount=50):
    all_details = KidsFashionScrape.objects.filter(percent__gte=discount).order_by('id')
    total_products = len(all_details)
    page = request.GET.get('page', 1)

    paginator = Paginator(all_details, 10)
    try:
        all_details = paginator.page(page)
    except PageNotAnInteger:
        all_details = paginator.page(1)
    except EmptyPage:
        all_details = paginator.page(paginator.num_pages)

    return render(request, 'kids-fashion.html',
                  {"scrapes": all_details, "total": total_products, "discount_per": discount})


def search(request):
    if request.GET:
        search_term = str(request.GET['search_term']).lower()  # get value that was passed in url
        android_search_result = AndroidScrape.objects.filter(product__icontains=search_term)
        iphone_search_result = IphoneScrape.objects.filter(product__icontains=search_term)
        computing_search_result = ComputingScrape.objects.filter(product__icontains=search_term)
        electronics_search_result = ElectronicsScrape.objects.filter(product__icontains=search_term)
        menfashion_search_result = MenFashionScrape.objects.filter(product__icontains=search_term)
        womenfashion_search_result = WomenFashionScrape.objects.filter(product__icontains=search_term)
        kidsfashion_search_result = KidsFashionScrape.objects.filter(product__icontains=search_term)
        healthandbeauty_search_result = HealthBeautyScrape.objects.filter(product__icontains=search_term)

        total_products = len(android_search_result) + len(computing_search_result) + len(
            electronics_search_result) + len(iphone_search_result) + len(menfashion_search_result) + len(
            womenfashion_search_result) + len(kidsfashion_search_result) + len(healthandbeauty_search_result)

        context = {"search_term": search_term,
                   "scrapes_1": android_search_result,
                   "scrapes_2": iphone_search_result,
                   "scrapes_3": computing_search_result,
                   "scrapes_4": electronics_search_result,
                   "scrapes_5": menfashion_search_result,
                   "scrapes_6": womenfashion_search_result,
                   "scrapes_7": kidsfashion_search_result,
                   "scrapes_8": healthandbeauty_search_result,
                   "total": total_products
                   }

        return render(request, 'search.html', context=context)
    else:
        return redirect('jumia_home')  # redirect to home page if there's no data in d url
