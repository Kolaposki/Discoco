"""
    name='views',
    project='discoco'
    date='4/9/2020',
    author='Oshodi Kolapo',
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .serializers import *
from jumia.models import AndroidScrape, IphoneScrape
from rest_framework.filters import SearchFilter, OrderingFilter


# View to list all products in d db, supports pagination
class ApiAndroidListView(ListAPIView):
    queryset = AndroidScrape.objects.all()
    serializer_class = AndroidSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('percent', 'product', 'price')


# View to list all products in d db, supports pagination
class ApiIphoneListView(ListAPIView):
    queryset = IphoneScrape.objects.all()
    serializer_class = IphoneSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('percent', 'product', 'price')