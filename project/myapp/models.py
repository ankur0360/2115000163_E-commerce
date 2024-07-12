from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    rating = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    catagory = models.CharField(max_length=50, null=True)
    availability = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
