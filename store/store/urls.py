"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products.views import index, shop, about, contact, shop_single, basket, basket_add, basket_remove, add_quantity_to_basket, remove_quantity_to_basket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('product/<int:product_id>/', shop_single, name='shop_single'),
    path('category/<int:category_id>/', shop, name='category'),
    path('page/<int:page_number>/', shop, name='paginator'),
    path('basket/', basket, name='basket'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('add_quantity_to_basket/<int:basket_id>/', add_quantity_to_basket, name='add_quantity_to_basket'),
    path('remove_quantity_to_basket/<int:basket_id>/', remove_quantity_to_basket, name='remove_quantity_to_basket'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

