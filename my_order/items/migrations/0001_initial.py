# Generated by Django 5.0.4 on 2024-05-05 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='furniture')),
                ('details', models.CharField(max_length=115)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/furniture/%Y/%m/')),
            ],
        ),
        migrations.CreateModel(
            name='TheItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time create')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='time of last update')),
                ('photo', models.ImageField(upload_to='photos/items/%Y/%m/')),
                ('location', models.ForeignKey(blank=True, max_length=25, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location', to='items.furniture', verbose_name='Furniture of the location')),
            ],
        ),
    ]
