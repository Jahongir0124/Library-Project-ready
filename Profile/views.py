from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from . forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from books.models import Category
from orders.models import *
from books.models import Books
from django.contrib.auth.forms import UserCreationForm
from . models import Profile
# Create your views here.
cat = Category.objects.all()
def profile(request):
    usr = User.objects.get(pk=request.user.id)
    user = Customer.objects.filter(customer=request.user)
    image = Profile.objects.filter(user=request.user.id)
    total = 0
    s = 0
    a = []
    for i in user:
        pr = Books.objects.get(pk=i.product.id)
        total+=pr.price
        s+=1
        a.append(s)
    return render(request,'profile.html',{'data':user,
                                          'cat':cat,
                                          'user':usr,
                                          'title':'Profil',
                                          'son':a,
                                          'total':total,
                                          "image":image})

def login_user(request):
    form = UserForm()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Tizimga muvafiqiyatli kirildi')
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Parol yoki boshqa parametrni qayta tekshiring')
    return render(request,'login.html',{'form':form,
                                        'title':'Kirish'})

def log_out(request):
    logout(request)
    return redirect('login')

def user_create(request):
    form = UserCreate()

    if request.POST:
        form = UserCreate(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            try:
                user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname,
                                                email=email)

                return redirect('login')
            except Exception as e:
                messages.add_message(request, messages.INFO, 'Bu nom bilan foydalauvchi yaratilgan')
        else:
            messages.add_message(request, messages.INFO, 'Parametrlarni to\'g\'ri kiritng')
    return render(request,'registrations.html',{'form':form,
                                                'title':'Ro\'yxatdan o\'tish'})

def saveImage(request):

    if request.POST:

        image = request.FILES.get('image',None)
        if image:
            profile = Profile.objects.create(
                    user=request.user,
                    image=image
                )
            return redirect('profile')
        else:
            messages.add_message(request, messages.INFO, 'Parametrlarni to\'g\'ri kiritng')
            return redirect('profile')