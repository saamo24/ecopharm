from django.db import models
from medicines.models import Medicine
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Order(models.Model):

    class Meta:
        db_table = 'Order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=13)
    medicines = models.ManyToManyField('medicines.Medicine') #, related_name='orders'
    # checkout_id = models.ForeignKey('order.Checkout', on_delete=models.CASCADE, related_name='checkout')

class Checkout(models.Model):
    
    class Meta:
        db_table = 'Checkout'
        verbose_name = _('Checkout')
        verbose_name_plural = _('Checkouts')

    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    medicine = models.ForeignKey('medicines.Medicine', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # class Meta:
    #     unique_together = ('order', 'medicine')

    def __str__(self):
        return self.medicine.name