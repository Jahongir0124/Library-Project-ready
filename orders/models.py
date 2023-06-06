from django.db import models
from books.models import *
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    customer = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    adress = models.CharField(max_length=300)
    product = models.ForeignKey(Books,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    
    

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
