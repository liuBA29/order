# Generated by Django 5.0.4 on 2024-05-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_furniture_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='theitem',
            name='is_actual',
            field=models.BooleanField(default=True),
        ),
    ]