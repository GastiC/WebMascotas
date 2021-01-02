# Generated by Django 3.0.4 on 2020-12-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugios', '0004_auto_20201231_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refugio',
            name='confirmacionEmail',
            field=models.EmailField(max_length=254, verbose_name='Repita Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='refugio',
            name='direccion',
            field=models.CharField(max_length=40, verbose_name='Domicilio'),
        ),
    ]