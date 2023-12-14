from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket, ProductInfo
from django.core.paginator import Paginator



#Функции = контроллеры = вьюхи


def index(request):
    baskets = Basket.objects.all()
    total_quantity = 0
    for basket in baskets:
        total_quantity += basket.quantity
    context = {
        'title': 'Главная',
        'total_quantity': total_quantity,
        'baskets': baskets
    }
    return render(request, 'products/index.html', context)


def about(request):
    baskets = Basket.objects.all()
    total_quantity = 0
    for basket in baskets:
        total_quantity += basket.quantity
    context = {
        'title': 'О нас',
        'total_quantity': total_quantity,
        'baskets': baskets
    }
    return render(request, 'products/about.html', context)


def contact(request):
    baskets = Basket.objects.all()
    total_quantity = 0
    for basket in baskets:
        total_quantity += basket.quantity
    context = {
        'title': 'Контакты',
        'total_quantity': total_quantity,
        'baskets': baskets
    }
    return render(request, 'products/contact.html', context)


def shop(request, category_id=None, page_number=1):
    baskets = Basket.objects.all()
    total_quantity = 0
    for basket in baskets:
         total_quantity += basket.quantity
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    products = products
    per_page = 6
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Каталог ',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
        'baskets': baskets,
        'total_quantity': total_quantity
    }
    return render(request, 'products/shop.html', context)



def basket(request):
    baskets = Basket.objects.all()
    total_summa = 0
    total_quantity = 0
    for basket in baskets:
        total_summa += basket.summa()
        total_quantity += basket.quantity
    context = {
        'title': 'Корзина товаров',
        'baskets': baskets,
        'total_summa': total_summa,
        'total_quantity': total_quantity,
         }
    return render(request, 'products/basket.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(product=product)
    if not baskets.exists():
        Basket.objects.create(product=product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def add_quantity_to_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_quantity_to_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.quantity -= 1
    basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def shop_single(request, product_id):
    baskets = Basket.objects.all()
    total_quantity = 0
    for basket in baskets:
        total_quantity += basket.quantity
    product = Product.objects.get(id=product_id)
    product_info = ProductInfo.objects.filter(product=product)
    context = {
        'title': 'Информация о продукте',
        'product': product,
        'product_info': product_info,
        'total_quantity': total_quantity
    }
    return render(request, 'products/shop-single.html', context)









