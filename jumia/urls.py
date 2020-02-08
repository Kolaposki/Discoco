"""
    name='urls',
    project='discoco'
    date='1/11/2020',
    author='Oshodi Kolapo',
"""

from . import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'jumia'

urlpatterns = [
    path('', views.jumia_home, name='jumia_home'),
    path('android/', views.android_scrape, name='android'),
    path('android/<int:discount>', views.android_scrape, name='android'),

    path('iphone/<int:discount>', views.iphone_scrape, name='iphone'),
    path('iphone/', views.iphone_scrape, name='iphone'),

    path('computing/<int:discount>', views.computing_scrape, name='computing'),
    path('computing/', views.computing_scrape, name='computing'),

    path('electronics/<int:discount>', views.electronics_scrape, name='electronics'),
    path('electronics/', views.electronics_scrape, name='electronics'),

    path('fashion/<int:discount>', views.fashion_scrape, name='fashion'),
    path('fashion/', views.fashion_scrape, name='fashion'),

    path('health-beauty/<int:discount>', views.health_beauty_scrape, name='health-beauty'),
    path('health-beauty/', views.health_beauty_scrape, name='health-beauty'),

    path('women-fashion/<int:discount>', views.women_fashion_scrape, name='women-fashion'),
    path('women-fashion/', views.women_fashion_scrape, name='women-fashion'),

    path('men-fashion/<int:discount>', views.men_fashion_scrape, name='men-fashion'),
    path('men-fashion/', views.men_fashion_scrape, name='men-fashion'),

    path('kids-fashion/<int:discount>', views.kids_fashion_scrape, name='kids-fashion'),
    path('kids-fashion/', views.kids_fashion_scrape, name='kids-fashion'),
]
