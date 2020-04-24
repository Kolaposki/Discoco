"""
    name='serializers',
    project='discoco'
    date='4/9/2020',
    author='Oshodi Kolapo',
"""
from rest_framework import serializers
from jumia.models import AndroidScrape, IphoneScrape


class AndroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidScrape
        fields = ['percent', 'product', 'price', 'old_price', 'product_url', 'img_url', ]


class IphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IphoneScrape
        fields = ['percent', 'product', 'price', 'old_price', 'product_url', 'img_url', ]
