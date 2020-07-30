import os

from django.db import models
from django.dispatch import receiver

from catalog.models import Catalog

class Photo(models.Model):
    name = models.CharField(max_length=255)
    catalog = models.ForeignKey(
        Catalog,
        models.CASCADE,
        verbose_name=('category_id'),
    )
    image = models.ImageField(upload_to='uploads')

@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)



def get_photos(item_id):
    pics = Photo.objects.filter(catalog_id = item_id)
    return pics

