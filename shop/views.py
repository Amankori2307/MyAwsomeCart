from django.shortcuts import render
from .models import Product, Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        phone = request.POST.get('phone') 
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
    # return HttpResponse("We are at contact")
    return render(request, 'shop/contact.html')

def tracker(request):
    # return HttpResponse("We are at tracker")
    return render(request, 'shop/tracker.html')

def search(request):
    return HttpResponse("We are at search")

def productview(request,myid):
    product = Product.objects.get(id = myid)
    print(product.product_name)
    # return HttpResponse("We are at product view")
    params = {'product' : product}
    return render(request,'shop/productview.html',params)

def checkout(request):
    return HttpResponse("We are at checkout")
