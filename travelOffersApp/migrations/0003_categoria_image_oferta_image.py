# Generated by Django 5.1.2 on 2024-11-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelOffersApp', '0002_pais_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]