# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GetDataOrder(models.Model):
    order_number = models.IntegerField(blank=True, null=True)
    price_in_usd = models.FloatField(db_column='price_in_USD', blank=True, null=True)  # Field name made lowercase.
    delivery_date = models.DateTimeField(blank=True, null=True)
    price_in_rub = models.FloatField(db_column='price_in_RUB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'get_data_order'
