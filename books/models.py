from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True)
    def __int__(self):
        return self.pk
    def __str__(self):
        return  self.name
    
    @property
    def getSlug(self):
        return self.slug


    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = "Kategoriyalar"
class Books(models.Model):
    cname = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Kategoriya nomi')
    name = models.CharField(max_length=150,verbose_name='Kitobning nomi')
    slug = models.SlugField(unique=True,null=True)
    description = models.TextField()
    author= models.CharField(max_length=200,verbose_name='Muallifi')
    publish_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    count = models.IntegerField()
    buy_count = models.IntegerField()
    photo = models.ImageField(upload_to='media/photo',null=True)
    fedback = models.IntegerField(default=0)
    
    

    # def slug(self):
    #     return slugify(self.name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('InfoBook', kwargs={'slug': self.slug})
    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = "Kitoblar"
class FedbackToBook(models.Model):


    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    



    def __str__(self):

        return self.book.name




class Discount(models.Model):
    pass


class Comments(models.Model):
    """docstring for ClassName"""
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    username = models.CharField(max_length=200)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.text



    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
        



