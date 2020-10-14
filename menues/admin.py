from django.contrib import admin
from .models import Category,Combo,Combo_Mashup,Menu


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','display_name']



@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ['id','display_name']



@admin.register(Combo_Mashup)
class Combo_MashupAdmin(admin.ModelAdmin):
    list_display = ['id','display_name']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','display_name']