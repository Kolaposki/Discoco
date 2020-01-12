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
    path('iphone/', views.iphone_scrape, name='iphone'),
]
