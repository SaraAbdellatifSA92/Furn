# Generated by Django 3.1.7 on 2021-03-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_products_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='customer',
        ),
        migrations.AddField(
            model_name='voucher',
            name='Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Skirts'), (2, 'Panatlon'), (3, 'T-shirt'), (4, 'SweatShirt'), (5, 'pullover')], null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='date_checked',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]