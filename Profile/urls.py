from django.urls import path
from .views import *
urlpatterns = [

    path('',login_user,name='login'),
    path('logout/',log_out,name='logout'),
    path('registration/',user_create,name='registration'),
    path('profile/',profile,name='profile'),
    path('save/',saveImage,name='image')
]