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
]
