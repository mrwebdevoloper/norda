
from django.urls import path
from .views import *
from main import views

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About),
    path('category/<int:id>/', Category),
    path('blog/', Blog),
    path('contact/', Contact),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('addtocart/<int:id>/', AddToCart, name='addtocart'),
    path('cart/', Cart),
    path('deletecart/<int:id>/', DeleteCart),
    path('buyurtmaberish/<int:id>/', BuyurtmaBerish),
    

    path('login/', Login),
    path('fav/', Fav),

    path('count-savatcha/', CountSavatcha),
    path('favourite/<int:pk>/', Favouritee, name='favourite'),
    path('logout/', Logout),
    path('register/', Register)
    
]