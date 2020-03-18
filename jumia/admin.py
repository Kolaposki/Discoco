from django.contrib import admin
from django.contrib.auth.models import Group
from jumia.models import *


class ScrapeDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class IphoneDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class AndroidDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class ComputingDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class FashionDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class HealthBeautyDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class MenFashionDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class WomenFashionDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


class KidsFashionDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')
    # list_display_links = ('id', 'product')
    list_per_page = 25
    search_fields = ('product',)
    list_filter = ('percent', 'price')


admin.site.register(ScrapeDetails, ScrapeDetailsAdmin)
admin.site.register(IphoneScrape, IphoneDetailsAdmin)
admin.site.register(AndroidScrape, AndroidDetailsAdmin)
admin.site.register(ComputingScrape, ComputingDetailsAdmin)
admin.site.register(FashionScrape, FashionDetailsAdmin)
admin.site.register(HealthBeautyScrape, HealthBeautyDetailsAdmin)
admin.site.register(MenFashionScrape, MenFashionDetailsAdmin)
admin.site.register(WomenFashionScrape, WomenFashionDetailsAdmin)
admin.site.register(KidsFashionScrape, KidsFashionDetailsAdmin)
admin.site.unregister(Group)
