# Generated by Django 5.1.2 on 2024-11-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelOffersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]