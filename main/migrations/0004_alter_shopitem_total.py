# Generated by Django 3.2.5 on 2021-08-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shop_shopitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
