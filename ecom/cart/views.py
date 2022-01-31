from itertools import product
from django.shortcuts import render
import decimal
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django. contrib import messages

def products(request):
    productss = Product.objects.all()
    return render(request, 'cart/products.html', {'productss':productss})


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        message=request.POST.get("message")
        email1="sandeepgowda2314@gmail.com"
        #resume=request.POST.get("resume")
        print("------------------------------------------------------------",name)
        print(email)
        print(mobile)
        print(message)
        data=contacts(name=name,Email=email,mobile=mobile,message=message)
        data.save()
        ctx = {
           'name' : name,
           'email':email,
           'mobile':mobile,
           'message' : message,
           }
        print(ctx)
        message=render_to_string('cart/mail.html',ctx)
        #message = render_to_string('mail.html', ctx)
        #data=contacts(name=name,Email=email,mobile=mobile,message=message)
        #data.save()
        #send_mail('Hi,your One Time Password is ',mobile,'gowdasandeep8105@gmail.com',[email1],fail_silently=False,)
        send_mail("Message from customer",message,'gowdasandeep8105@gmail.com',[email1],fail_silently=False,)
        print('++++++++++++++++++++++++Email sent+++++++++++++++++++++++++++++')
        #print(resume)  
        return render (request,"cart/contact.html")
    else:
        return render (request,"cart/contact.html")
def search(request):
    if request.method=="POST":
        searched=request.POST.get('searched')
        venues=Product.objects.filter(productname__contains=searched)
        return render(request,"cart/add.html",{'searched':searched,"venues":venues})
    else:
        return render(request,"cart/add.html")
def cart(request):
    cart_products = Cart.objects.all()
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",cart_products)

    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all()]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

    # Customer Addresses
    #addresses = Address.objects.filter(user=user)

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
        #'addresses': addresses,
    }
    #return render(request, 'store/cart.html', context)
    return render(request,"cart/cart.html",{"cart_products":cart_products,"context":context})

def add_to_cart(request):
    #user = request.user
    product_id = request.GET.get('prod_id')
    #product_name = request.GET.get('prod_name')
    #product_price = request.GET.get('prod_price')
    #product_image = request.GET.get('prod_image')
    #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    product = get_object_or_404(Product, id=product_id)
    print("********************************************************************",product)
    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=product_id)
    if item_already_in_cart:
        cp = get_object_or_404(Cart, product=product_id)
        cp.quantity += 1
        cp.save()
    else:
        Cart(product=product).save()
    
    return redirect('cart')

#def remove(request):
    #c=get_object_or_404(Cart,id=cart_id)

