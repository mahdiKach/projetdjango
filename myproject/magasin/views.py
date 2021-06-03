import json
from time import timezone

from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from .forms import ProduitForm, CreateUserForm

# Create your views here.
from .models import *


def index(request):
    list = Produit.objects.all()
    return render(request, 'vitrine.html', {'list': list})
def majProd(request):
    if request.method == "POST":

        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produits')
    else:

        form = ProduitForm()
    return render(request,'majProduits.html',{'form':form})
def chariot(request):
    if request.user.is_authenticated:
        client=request.user.client
        order,created=Order.objects.get_or_create(client=client,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_chariot_total':0,'get_chariot_items':0}

    context = {'items':items,'order':order}
    return render(request, 'chariot.html', context)


def checkout(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_chariot_total': 0, 'get_chariot_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)
def produitdetail(request,pk):
    products = Produit.objects.get(id=pk)
    context= {'products':products}
    return render(request,"details.html",context)
def home(request):
    context={}
    return render(request,"magasin.html",context)

def Dashboard (request):
    orders=OrderItem.objects.all()
    clients=Client.objects.all()
    context={'orders':orders,'clients':clients}
    return render(request,"dashboard.html",context)
def loginn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.groups.add(group)
            Client.objects.create(
                user=user,
                nom=user.username,
            )

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)
