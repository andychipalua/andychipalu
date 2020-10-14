from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField
    display_name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)
    display_image_url = models.ImageField(default=None)
    priority = models.IntegerField(default=1)

class Menu(models.Model):
    HAS_COMBO = [(0,'No'),(1,'Yes')]
    id = models.IntegerField
    display_name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    display_images_url = models.ImageField(default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    categories = models.ManyToManyField('Category',blank=True)
    has_combo = models.BooleanField(choices=HAS_COMBO,default = 0)
    combos = models.ManyToManyField('Combo',blank=True)

class Combo(models.Model):
    id = models.IntegerField
    display_name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    
    display_images_url = models.ImageField(default=None)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    combo_items = models.ManyToManyField('Combo_Mashup',blank=True)

class Combo_Mashup(models.Model):
    id = models.IntegerField
    display_name = models.CharField(max_length=30)
    category_items = models.IntegerField
    combo_id = models.IntegerField
    category_id = models.IntegerField



