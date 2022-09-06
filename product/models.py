from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photo',
                              blank=True)
    manufacturer = models.CharField(max_length=300,
                                    blank=True)
    price_in_dollars = models.DecimalField(max_digits=6,
                                           decimal_places=2)
from datetime import datetime

class ProductDetails(models.Model):
    status_choices = (
        (1, "Open"),
        (2, "Repaired"),
        (3, "Closed"),

    )
    product_name = models.CharField(max_length=80, verbose_name="Product Name", blank=False, null=False)
    model_name = models.CharField(max_length=80, verbose_name="Model Name", blank=False, null=False)
    serial_no = models.CharField(max_length=80, verbose_name="Serial No.", blank=False, null=False)
    mobile = models.BigIntegerField(blank=False, null=False)
    name = models.CharField(max_length=80, blank=False, null=False)
    entry_date = models.DateTimeField(default=datetime.now(), blank=True)
    completed_date = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.IntegerField(choices=status_choices, default=1)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
class Student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


    class Meta:
        ordering = ['id']



