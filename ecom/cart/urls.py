from django.urls import path
from . import views

urlpatterns = [

    path('', views.products, name='products'),
    path("search",views.search,name="search"),
    path("contact",views.contact,name="contact"),
    path('cart',views.cart,name="cart"),
    path("add-to-cart",views.add_to_cart,name='add-to-cart')

]