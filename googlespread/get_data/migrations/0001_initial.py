# Generated by Django 4.0.5 on 2022-06-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(db_index=True, verbose_name='Номер заказа')),
                ('price_in_USD', models.FloatField(verbose_name='Стоимость в долларах')),
                ('delivery_date', models.DateTimeField(verbose_name='Срок поставки')),
                ('price_in_RUB', models.FloatField(verbose_name='Стоимость в рублях')),
            ],
        ),
    ]
