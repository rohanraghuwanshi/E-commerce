from django.db import models

# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=500)


    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'