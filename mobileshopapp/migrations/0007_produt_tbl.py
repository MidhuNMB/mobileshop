# Generated by Django 4.2.2 on 2023-10-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileshopapp', '0006_delete_produt_tbl'),
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
                ('photo', models.CharField(max_length=50)),
            ],
        ),
    ]