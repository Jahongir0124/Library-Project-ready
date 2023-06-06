from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.conf import settings



def set_language(request,code):
    translation.activate(code)
    old_full_url = request.META.get('HTTP_REFERER', '/')
    old_url = f"/{'/'.join(old_full_url.split('/')[3:])}"
    prefix_exists = False
    for language in settings.LANGUAGES:
        if f"/{language[0]}/" in old_url:
            prefix_exists = True
    if not prefix_exists and code != settings.LANGUAGE_CODE:
        new_url = F"/{code}{old_url}"
    elif code == settings.LANGUAGE_CODE:
        new_url = old_url.replace(f"/{old_url.split('/')[1]}/", "/")
    else:
        new_url = old_url.replace(f"/{old_url.split('/')[1]}/", f"/{code}/")
    return redirect(new_url)