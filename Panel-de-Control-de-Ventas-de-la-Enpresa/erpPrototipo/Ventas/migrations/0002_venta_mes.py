# Generated by Django 5.0.3 on 2024-03-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='Mes',
            field=models.IntegerField(default=3),
        ),
    ]
