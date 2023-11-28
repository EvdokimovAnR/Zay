from django.shortcuts import render


def order_create(request):
    return render(request, 'orders/order-create.html')