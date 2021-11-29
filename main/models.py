from typing import Text
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.http import JsonResponse

class Categories(models.Model):
    name = models.CharField(max_length=255) 
    rasm = models.ImageField(upload_to= 'category', null=True, blank=True)

    def __str__(self):
        return self.name



class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to='products')

    def __str__(self):
        return self.name

class Banners(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to= 'banners')

    def __str__(self):
        return self.title



class Shop(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


class Favourite(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.pk)

class Favouriteitem(models.Model):
    fav = models.ForeignKey(Favourite, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk)


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


class UserPhone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.user.first_name
