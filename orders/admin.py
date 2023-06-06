from django.contrib import admin
from . models import *
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_time'
    list_display = ['customer', 'adress', 'product', 'create_time']
    list_filter = ('customer', 'product')



admin.site.register(Customer,OrderAdmin)

