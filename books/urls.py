from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='home'),
    path('book/<slug:slug>/', views.InfoBook.as_view(), name='unique_slug'),
    path('category/<slug:slug>/', views.Categorybook.as_view(), name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('discount/', views.DisCounts.as_view(), name='discount'),
    path('new/', views.NewBooks.as_view(), name='new'),
    path('fedback',views.fedbackView,name="fedback"),
    path('comment',views.comment,name="comment")
]