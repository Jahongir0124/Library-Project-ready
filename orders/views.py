from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,DetailView
from .models import Customer
from .form import *
from django.contrib import messages
from books.models import Books,Category
from django.http import HttpResponse
cat = Category.objects.all()
def order(request,b_id):
    if request.user.is_authenticated:
        customer = Customer()
        form = CustomerForm()
        product = Books.objects.get(pk=b_id)
        order = Customer.objects.filter(customer=request.user)
        a = []
        if order:
             for i in order:
                a.append(i.product)
             if product in a:
                messages.add_message(request, messages.INFO, 'Siz bu mahsulotga buyurtma bergansiz')
                return redirect('home')
             else:
                if request.POST:
                    order = Customer(customer=request.user, product=product, adress=request.POST['adress'])
                    order.save()
                    product.count-=1
                    product.save()
                    messages.add_message(request, messages.INFO, 'Buyurtma r\'oyxatga olindi')
                    return redirect('home')
        else:
                if request.POST:
                    order = Customer(customer=request.user, product=product, adress=request.POST['adress'])
                    order.save()
                    product.count-=1
                    product.save()
                    messages.add_message(request, messages.INFO, 'Buyurtma r\'oyxatga olindi')
                    return redirect('home')
        a.clear()
        return render(request,'form.html',{'form':form,
                                        'cat':cat,
                                        'pr':product})
    else:
        messages.add_message(request, messages.INFO,"Login qiling")
        return redirect('login')


def deleteOrder(request,id):

    order = Customer.objects.get(pk=id)
    order.delete()
    return redirect('profile')









    