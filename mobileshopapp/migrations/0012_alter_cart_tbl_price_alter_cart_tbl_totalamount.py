# Generated by Django 4.0.4 on 2023-10-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileshopapp', '0011_cart_tbl_totalamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_tbl',
            name='price',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cart_tbl',
            name='totalAmount',
            field=models.IntegerField(),
        ),
    ]