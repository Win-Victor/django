from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)  # varchar(64), уникальные значения
    description = models.TextField(blank=True, null=True)

    # text - тип данных, blank=True - может быть пустым, default null, т.е. необязательное для заполнение поле

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)  # путь для расположения файла фото
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # цифр до "," и после
    quantity = models.PositiveIntegerField(default=0)  # какое-то неотрицательное число
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    # ForeignKey - ключ к таблице ProductCategory, действия при удалении (/ SET_NULL / )
    def __str__(self):
        return f'{self.name} | {self.category.name} | {self.image}'
