from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey("store.Category", default=1, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='Products/')
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name