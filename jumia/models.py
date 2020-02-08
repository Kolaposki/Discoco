from django.db import models


# Create your models here.


class ScrapeDetails(models.Model):
    percent = models.CharField(max_length=4)
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class IphoneScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class AndroidScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class ComputingScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class ElectronicsScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class FashionScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class HealthBeautyScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class MenFashionScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class WomenFashionScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product


class KidsFashionScrape(models.Model):
    percent = models.IntegerField()
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    product_url = models.URLField(max_length=300, unique=True)
    img_url = models.URLField(max_length=300)

    def __str__(self):
        return self.product
