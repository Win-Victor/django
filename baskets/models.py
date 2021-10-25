from django.db import models

from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def total(self):
        baskets = Basket.objects.filter(user=self.user)
        total_quantity = sum(basket.quantity for basket in baskets)
        total_sum = sum(basket.sum() for basket in baskets)
        return {'total_quantity': total_quantity, 'total_sum': total_sum}
