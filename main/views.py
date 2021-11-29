from django.http import request
from django.contrib.auth import authenticate, login, logout
from main import models
from django.contrib import messages
from main.models import *
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):

    products = Products.objects.all()
    category = Categories.objects.all()
    banners = Banners.objects.all()

    context = {
        'products' : products,
        'categories' : category,
        'banners': banners
    }

    return render(request, 'home.html', context)

@login_required
def About(request):

    return render(request, 'about.html')

@login_required
def Category(request, id):

    products = Products.objects.filter(category_id=id)
    category = Categories.objects.all()
   

    context = {
        'products' : products,
        'categories' : category,
        
    }
    return render(request, 'shop.html', context)

@login_required
def Blog(request):
    return render(request, 'blog.html')

@login_required
def Contact(request):
    return render(request, 'contact.html')


class ProductDetail(DetailView) :
    model = Products
    
    template_name = 'product-details.html'
    context_object_name = 'product'


def AddToCart(request, id):
    user = request.user

    try:
        shop = Shop.objects.create(client=user, status=0)
    except:
        shop = Shop.objects.create(client = user)
    product = Products.objects.get(id=id)
    if product.discount:
        ShopItem.objects.create(shop=shop, product=product, quantity=1, total=product.discount)
        shop.total += product.discount
    else:
        ShopItem.objects.create(shop=shop, product=product, quantity=1, total=product.price)
        shop.total += product.price
    shop.save()
    return redirect('/')


def Cart(request):
    shop = Shop.objects.filter(status=0)
    products = ShopItem.objects.filter(shop__client=request.user, shop__status=0 )
    context = {
        'products':products,
        'shop':shop[0],
    }
    return render (request, 'cart.html', context)



def Favouriteee(request):

    return render(request, 'wishlist.html')




def Favouritee(request, pk):
    user = request.user

    try:
        fav = Shop.objects.create(client=user, status=0)
    except:
        fav = Shop.objects.create(client = user)
    product = Products.objects.get(id=id)
        
    fav.save()
    return redirect('/')

def Fav(request):

    return render(request, 'wishlist.html')


def DeleteCart(request, id):

    item = ShopItem.objects.get(id=id)
    item.delete()


    return redirect('/cart/')



def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user )
            return redirect('/')
        else:
            return redirect('/login/')
    else:

        return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Tizimdan chiqish muvaffaqiyatli yakunlandi")
    return redirect('/login')

def Register(request):
    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']
        ism = r['ism']
        fam = r['fam']
        phone = r['phone']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/login/')
        else:
            user = User.objects.create(username=username, password=password, first_name=ism, last_name=fam)
            UserPhone.objects.create(user=user, phone=phone)
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'register.html')

def BuyurtmaBerish(request, id):
    shop = Shop.objects.get(id=id)
    shop.status=1
    shop.save()

    return redirect('/')

def CountSavatcha(request):
    count = ShopItem.objects.filter(shop__client=request.user, shop__status=0)
    s = 0
    for c in count:
        s += c.total

    data = {
        'count': count.count(),
        'total': s
    }


    return JsonResponse(data)