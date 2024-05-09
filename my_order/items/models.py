from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



class Furniture(models.Model):
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='furniture')
    details = models.CharField(max_length=115, blank=True, null=True)

    photo = models.ImageField(upload_to="photos/furniture/%Y/%m/", blank=True, null=True)

    def __str__(self):
        return self.slug





class TheItem(models.Model):
    name = models.CharField(max_length=35)
    location = models.ForeignKey(Furniture, max_length=25, blank=True, null=True, on_delete=models.PROTECT,
                                 verbose_name="Furniture of the location", related_name="location")

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time create")
    time_update = models.DateTimeField(auto_now=True, verbose_name="time of last update")
    photo = models.ImageField(upload_to="photos/items/%Y/%m/")

    def __str__(self):
        return self.name
