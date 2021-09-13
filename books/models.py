from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    phone = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=True)
    discount = models.BooleanField(default=0, blank=False)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


#     def __str__(self):
#         return self.first_name + " " + self.last_name
#

class Seller(models.Model):
    POSITION_LIST = [
        ('Trainee', "Стажер"),
        ('Salesman', "Продавец"),
        ('Oldest salesman', "Старший продавец"),
        ('Supervisor', "Руководитель")
    ]
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    phone = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=True)
    position = models.CharField(max_length=64, blank=False, default='Trainee', choices=POSITION_LIST)
    img = models.ImageField(upload_to='seller_img/%Y/%m/%d', blank=True)
    recruitment = models.DateField(verbose_name="Принятие на работу")

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"


#     def __str__(self):
#         return f'{self.first_name} {self.last_name} {self.position }'
#

class Book(models.Model):
    GENRE_LIST = [
        ('Detective', 'Детектив'),
        ('Thriller', 'Триллер'),
        ('Novel', 'Роман'),
        ('Psychology', 'Психолоия')
    ]

    name_product = models.CharField(blank=False, max_length=64)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    genre = models.CharField(max_length= 64, blank=False, choices=GENRE_LIST, default='Detective')
    img = models.ImageField(upload_to='books_img/%Y/%m/%d', blank=True, default='media/img.png')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


#     def __str__(self):
#         return self.category + ' ' + self.name_product
#

class Order(models.Model):
    customer = models.ForeignKey("Customer",
                                 on_delete=models.CASCADE,
                                 related_name='orders',
                                 related_query_name='orders',
                                 verbose_name='Покупатель')

    seller = models.ForeignKey("Seller",
                               on_delete=models.CASCADE,
                               related_name='orders',
                               related_query_name='order',
                               verbose_name='Продавец')

    product = models.ForeignKey('Book',
                                on_delete=models.CASCADE,
                                related_name='orders',
                                related_query_name='order',
                                verbose_name='Товар')

    date = models.DateField(auto_now_add=True, verbose_name="Время продажи")
    total = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                blank=False,
                                default=0,
                                verbose_name='Сумма продажи')

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

#     def __str__(self):
#         return f'Продавец: {self.seller} Покупатель: {self.customer} {self.total}'
