from django.urls import path
from .views import *
urlpatterns = [
    path('<int:b_id>/',order,name='order'),
    path('delete/''<int:id>/',deleteOrder,name='deleteOrder')
]