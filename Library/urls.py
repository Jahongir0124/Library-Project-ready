
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve 
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . set_language import set_language
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_language/''<str:code>',set_language,name='set_language'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]


urlpatterns += i18n_patterns(
    path('',include('books.urls')),
    path('orders/',include('orders.urls')),
    path('account/',include('Profile.urls')),
    prefix_default_language=False
)