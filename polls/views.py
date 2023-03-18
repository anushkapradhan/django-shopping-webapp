from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from .models import  diwaliProducts, ganpatiProducts , christmasProducts 
from .models import siteProducts, MyCart, MyOrder
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request, *args, ** kwargs,):
    if request.method == 'POST':
        user_name = request.POST.get('user_name',False)
        password = request.POST['password']
        user = auth.authenticate(username = user_name, password=password)
        print(request.user)
        if user is not None:
            auth.login(request, user)
            return redirect('category')
        else :
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request, *args, ** kwargs):
    if request.method == 'POST' :
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 =request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            if(User.objects.filter(email=email).exists()):
                messages.info(request,'email already exists')
                return redirect('signup')
            elif (User.objects.filter(username=user_name).exists()):
                messages.info(request,'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=user_name, email=email, password=password1)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
        
    return render(request, 'signup.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')

def category(request):
    return render(request, 'category.html')

def ganpatiFest(request):
    Gproduct = siteProducts.objects.all()
    return render(request, 'ganpatiFest.html',{'Gproduct':Gproduct})

def diwaliFest(request):
    Dproduct = siteProducts.objects.all()
    return render(request, 'diwaliFest.html',{'Dproduct':Dproduct})

def christmasFest(request):
    Cproduct = siteProducts.objects.all()
    return render(request, 'christmasFest.html',{'Cproduct':Cproduct})

def description(request, id, *args, **kwargs):
    product = siteProducts.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'description.html', context)

def addCart(request, id, *args, **kwargs):
    if (not request.user.is_authenticated):
        return redirect('login')
    user_obj = User.objects.filter(username=request.user)
    product_obj = siteProducts.objects.filter(id=id)
    check = MyCart.objects.filter(user=request.user,product_id=id)
    if len(check) != 0:
        print("Product Exits!!")
    else:
        obj = MyCart.objects.create(
            user=user_obj[0], product_id=product_obj[0], added_date=datetime.now())
        obj.save()
        print("saved in cart")
    return redirect('cart')

def remove(request, id,*args, **kwargs):
    cart_obj = MyCart.objects.get(product_id= id)
    cart_obj.delete()
    return redirect('cart')

def cart(request, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    cart_obj = MyCart.objects.filter(user=user_obj)
    img = list()
    for item in cart_obj:
        proObj = siteProducts.objects.get(id=item.product_id.id)
        img.append(proObj)

    con = zip(cart_obj, img)
    context = {
        'con': con
    }
    return render(request, "cart.html", context)

def order(request,id, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    print(id)
    product_obj = siteProducts.objects.get(id = id)
    obj = MyOrder.objects.create(user = user_obj, product_id = product_obj)
    obj.save()
    cart_obj = MyCart.objects.filter(product_id = product_obj)
    cart_obj.delete()
    # product_obj.instock = False
    product_obj.save()
    return redirect('cart')

def order_view(request, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    order_obj = MyOrder.objects.filter(user=user_obj)
    img = list()
    for item in order_obj:
        proObj = siteProducts.objects.get(id=item.product_id.id)
        img.append(proObj)

    con = zip(order_obj, img)
    context = {
        'con': con
    }
    return render(request,"order.html",context)

def aboutus(request) :
    return render(request, 'about.html')