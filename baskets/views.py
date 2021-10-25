from django.shortcuts import HttpResponseRedirect

from products.models import Product
from baskets.models import Basket


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        if product.quantity > 0:
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            pass
    else:
        basket = baskets.first()
        if product.quantity > basket.quantity:
            basket.quantity += 1
            basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
