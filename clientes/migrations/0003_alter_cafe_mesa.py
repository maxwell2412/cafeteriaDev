# Generated by Django 4.2.7 on 2023-12-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_cafe_cafe_pedido_remove_cafe_consumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='mesa',
            field=models.IntegerField(),
        ),
    ]
