from django.db import models

# Create your models here.

        
class HTMLBlock(models.Model):
    BLOCK_CATAGORY = [{"text","Text"},{"html","HTML"},{"slide","Slide"}]
    cid = models.IntegerField
    name = models.CharField(max_length=40)
    body = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    submitter = models.CharField(max_length=30)