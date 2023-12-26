from django.shortcuts import render
from .models import Product, Brand, Category
from .filters import ProductFilter
from django.contrib import messages

def all_products(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request,'shop/products.html',{
        'filter': f,
        'brands': Brand.objects.filter(favorite=True),
        'categories': Category.objects.all()
    })

def brand_products(request, brand):
    brandObj = Brand.objects.get(slug=brand)
    products=Product.objects.filter(brand=brandObj)
    return render(request,'shop/brand_product.html',{
        'brand': brandObj,
        'products': products,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
    })

def category_products(request, category):
    catObj = Category.objects.get(slug=category)
    products=Product.objects.filter(category=catObj)
    return render(request,'shop/category_product.html',{
        'category': catObj,
        'products': products,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
    })



def search_products(request):
    q = request.GET.get('q')
    if q is None:
        messages.error(request, 'please enter somthing to search')
    Product_list_1 = Product.objects.filter(name__icontains=q)
    Product_list_2 = Product.objects.filter(brand__name__icontains=q)
    Product_list_3 = Product.objects.filter(category__name__icontains=q)
    return render(request, 'shop/search.html',{
        'products' :  Product_list_1.union(Product_list_2,Product_list_3),
        'brands' : Brand.objects.filter(name__icontains=q),
        'Category' : Category.objects.filter(name__icontains=q),
        'q': q,
        'total_item' : Product_list_1.count() + Product_list_2.count() + Product_list_3.count()
    })