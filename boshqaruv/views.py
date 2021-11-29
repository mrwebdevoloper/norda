from django.http import request
from django.shortcuts import redirect, render
from main.models import *
from django.contrib.auth.models import User


def Home(request):
    return render(request, 'Admin/index.html')

def Client(request):

    clients = User.objects.filter(is_superuser=False)

    context = {
       'clients':clients 
    }

    return render(request, 'Admin/data-table.html', context)

def Shops(request):

    shops = Shop.objects.filter(status=1)
    context = {
        'shops':shops
    }
    return render(request, 'Admin/shop.html', context)


def Shopitem(request, pk):
    shopitem = ShopItem.objects.filter(shop_id=pk)

    context = {
        'shopitem':shopitem
    }


    return render(request, 'Admin/shop-item.html', context)

def Qabul(request, pk):
    shop = Shop.objects.get(id=pk)
    shop.status = 2
    shop.save()

    context = {
        'shop':shop
    }

    return redirect('/boshqaruv/shop/')

def Ochirish(request, pk):
    shop = Shop.objects.get(id=pk)
    shop.status = 3
    shop.save()

    return redirect('/boshqaruv/shop/')


def Qabulqil(request):

    shops = Shop.objects.filter(status=2)
    context = {
        'shops':shops
    }
    return render(request, 'Admin/qabul.html', context)

def Qaytar(request):

    shops = Shop.objects.filter(status=3)
    context = {
        'shops':shops
    }
    return render(request, 'Admin/qaytar.html', context)


def Buyurtma(request):

    shops = Shop.objects.filter(status=0)
    context = {
        'shops':shops
    }
    return render(request, 'Admin/buyurtmaberishkk.html', context)


