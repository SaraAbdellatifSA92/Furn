# Generated by Django 3.1.7 on 2021-03-06 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210306_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voucher',
            old_name='Name',
            new_name='name',
        ),
    ]
