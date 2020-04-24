"""
    name='urls',
    project='discoco'
    date='4/9/2020',
    author='Oshodi Kolapo',
"""

from .views import *
from django.urls import path

app_name = 'jumia'
# url : discoco/jumia/api/

urlpatterns = [
    path('android/', ApiAndroidListView.as_view(), name='api_android'),
    path('iphone/', ApiIphoneListView.as_view(), name='api_iphone'),
]
