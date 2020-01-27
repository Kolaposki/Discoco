from django.contrib import admin

# Register your models here.
from jumia.models import *


class ScrapeDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')


class IphoneDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')


class AndroidDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')


class ComputingDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'percent', 'price', 'product_url')


admin.site.register(ScrapeDetails, ScrapeDetailsAdmin)
admin.site.register(IphoneScrape, IphoneDetailsAdmin)
admin.site.register(AndroidScrape, AndroidDetailsAdmin)
admin.site.register(ComputingScrape, ComputingDetailsAdmin)
