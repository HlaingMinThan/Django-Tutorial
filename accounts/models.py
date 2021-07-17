from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name        


class Product(models.Model):
    category=(
        ('indoor','In Door'),
        ('outdoor','Out Door')
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=category)
    description=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name   