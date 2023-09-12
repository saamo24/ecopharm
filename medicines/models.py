from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Medicine(models.Model):

    class Meta:
        db_table = 'Medicines'
        verbose_name = _('Medicine')
        verbose_name_plural = _('Medicines')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.URLField(max_length=255)
    #description = models.TextField()

# class Checkout(models.Model):
#     class Meta:
#         db_table = 'checkout'
#         verbose_name = _('checkout')
#         verbose_name_plural = _('checkout')

#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     order_id = ForeignKey(Order, on_delete=models.CASCADE)
#     medicine_id = ForeignKey(Medicine, on_delete=models.CASCADE)


# class Order(models.Model):
#     class Meta:
#         db_table = 'orders'
#         verbose_name = _('order')
#         verbose_name_plural = _('orders')

#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     items = models.ForeignKey(Checkout, on_delete=models.CASCADE) #related_name§
#     full_name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     tel = models.CharField(max_length=13)
