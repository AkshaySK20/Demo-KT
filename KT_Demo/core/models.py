from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class CarDetails(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Car Detail"
        verbose_name_plural = "Car Details"

    def __str__(self):
        return self.title

