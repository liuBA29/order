# Generated by Django 5.0.4 on 2024-05-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='details',
            field=models.CharField(blank=True, max_length=115, null=True),
        ),
    ]