import uuid
from django.utils.timezone import now
from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField('Тип продукта')
    count_field = models.CharField('Количество', max_length=40)
    new_price = models.IntegerField('Новая цена')
    discount = models.IntegerField('Скидка')
    def __str__(self):
        return f'{self.count_field} {self.type} is now {self.new_price} vs {self.new_price}'
    def type_by_type_id(self):
        if self.type == 1:
            type_name = 'followers'
        elif self.type == 2:
            type_name = 'likes'
        elif self.type == 3:
            type_name = 'views'
        elif self.type == 4:
            type_name = 'auto-likes'
        elif self.type == 11:
            type_name = 'followers'
        elif self.type == 12:
            type_name = 'likes'
        elif self.type == 13:
            type_name = 'views'
        elif self.type == 21:
            type_name = 'followers'
        elif self.type == 22:
            type_name = 'likes'
        elif self.type == 23:
            type_name = 'views'
        elif self.type == 31:
            type_name = 'followers'
        elif self.type == 32:
            type_name = 'likes'
        elif self.type == 33:
            type_name = 'views'
        else:
            type_name = '?'
        return type_name
    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField('UUID', default=uuid.uuid4, editable=False)
    amount = models.IntegerField('Количество')
    type = models.IntegerField('Тип продукта')
    email = models.CharField('E-mail клиента', max_length=50)
    link = models.CharField('Инста клиента', max_length=50)
    created = models.DateTimeField('Создан', default=now)
    paid = models.DateTimeField('Оплачен', null=True)
    client_ip = models.CharField('IP Клиента', max_length=40)
    status = models.IntegerField('Статус заказа', default=0)
    approve_order = models.IntegerField('Какая то непонятная хуйня из стока', default=0)

    def __str__(self):
        return f'Order #{self.id} with UUID {self.uuid}, {self.amount} of {self.type} created at {self.created} and paid(or not paid) {self.paid}, from IP {self.client_ip} with status {self.status}'
