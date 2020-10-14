from django.contrib import admin
from .models import HTMLBlock
# Register your models here.

@admin.register(HTMLBlock)
class HTMLBlockAdmin(admin.ModelAdmin):
    list_display = ['cid','name','create_date','update_date','submitter']
