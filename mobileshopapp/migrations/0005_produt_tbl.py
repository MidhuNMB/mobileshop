# Generated by Django 4.2.2 on 2023-10-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileshopapp', '0004_remove_useraccount_tbl_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='produt_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('colour', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=500)),
            ],
        ),
    ]
