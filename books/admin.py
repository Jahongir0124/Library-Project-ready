from django.contrib import admin
from .models import *




class BooksAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    list_display = ['id','cname','name','author','photo']
    list_display_links = ('name','cname')
    list_filter = ('cname','name')
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Books,BooksAdmin)
# admin.site.register(Comments)
