from django.shortcuts import render
from .models import Product, Brand, Category, ProductImage,ProductReview,Seller
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


def seller_products(request, id):
    seller = Seller.objects.get(id=id)
    products=Product.objects.filter(seller=seller)
    return render(request,'shop/seller_product.html',{
        'seller': seller,
        'products': products,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all(),
        'seller': Seller.object.all(),
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
        'categories' : Category.objects.filter(name__icontains=q),
        'q': q,
        'total_item' : Product_list_1.count() + Product_list_2.count() + Product_list_3.count()
    })
def product_detail (request,slug):
    product = Product.objects.get(slug=slug)
    sim_cat_products =Product.objects.filter(category=product.category).exclude(slug=slug).order_by('?')[:2]
    reviews = ProductReview.objects.filter(product=product)
    images = ProductImage.objects.filter (product=product)

    return render(request,'shop/product_detail.html',{
        'product': product,
        'images': images,
        'reviews': reviews,
        'sim_cat_products':  sim_cat_products
    })