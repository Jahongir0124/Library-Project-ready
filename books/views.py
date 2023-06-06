from re import template
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView,DetailView
from .models import *
import json
from django.http import HttpResponseBadRequest, JsonResponse

# Create your views here.


class Index(ListView):
    model = Books
    paginate_by = 3
    context_object_name = 'book_list'
    template_name = 'home.html'
    category = Category.objects.all()
    for c in category:
        print(c.name)
    extra_context = {'title':'Bosh sahifa','cat':category}

    def get_queryset(self):

        book = Books.objects.all().order_by('-fedback')
        return book




class Categorybook(ListView):
    model = Books
    context_object_name = 'book_list'
    paginate_by = 3
    template_name = 'home.html'
    cat = Category.objects.all()
    extra_context = {'cat': cat}
    def get_queryset(self):
        category = Category.objects.filter(slug=self.kwargs['slug'])
        book = Books.objects.filter(cname=self.kwargs['slug'])
        return book
class DisCounts(ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'discount.html'
    def get_queryset(self):
        return HttpResponse('Hozirda Chegirmalar mavjud emas')
class InfoBook(ListView):
    model = Books
    context_object_name = 'book_info'
    template_name = 'book_info.html'
    category = Category.objects.all()
    extra_context = {'cat': category}
    def get_queryset(self):
        self.extra_context['url'] = self.request.build_absolute_uri()
        data = Books.objects.get(slug=self.kwargs['slug'])
        coments = Comments.objects.filter(book=data)
        self.extra_context['com'] = coments
        return data
class Search(ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'home.html'
    try:
        @method_decorator(csrf_exempt)
        def get_queryset(self):
            if 'q' in self.request.GET:
                data = self.request.GET['q']
                if len(data) > 0:
                    if data.isdigit():
                        book = Books.objects.filter(price=data)
                        return book
                    else:
                        book = Books.objects.filter(Q(name__contains=data) | Q(description__contains=data))
                        return book
                elif len(data) == 0:
                    return reverse('home')
                else:
                    return HttpResponse('Qidiruv kalit so\'zini kiriting')
            else:
                return reverse('home')
    except Exception as e:
        pass
    
class NewBooks(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'book_list'
    paginate_by = 3
    def get_queryset(self):
        book = Books.objects.all().order_by('-created_time')[:5]
        return book


@csrf_exempt
def fedbackView(request):
    if request.POST:
        try:
            user = request.user
            book = Books.objects.get(pk=request.POST['id'])
            fedbackcha = FedbackToBook.objects.filter(book=book).filter(user=request.user)
            print(fedbackcha)
            if fedbackcha:
                print("Xato")
                return JsonResponse({'status':"Error"})

            else:
                book.fedback+=1
                feeed = FedbackToBook.objects.create(
                    book=book,
                    user=user
                )
                book.save()
                return JsonResponse({'status':"Sucess"})
        except Exception as e:
            print(e)
    return redirect('home')


def comment(request):

    user = request.user
    text = request.POST.get('t')
    url = request.POST.get('url')
    idka = request.POST.get("b_id")
    book = Books.objects.get(pk=idka)
    email = request.user.email
    fullName = request.user.first_name+" "+request.user.last_name
    if url:
        coments = Comments.objects.create(
                username=fullName,
                book=book,
                text=text,
                email=email
            )
        return redirect(url)

    else:
        return redirect('home')










