from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.CarDetails)
class cardetailsAdmin(admin.ModelAdmin):
    list_display = ['id','title','brand']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]