from versatileimagefield.fields import VersatileImageField
from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField('Image', upload_to='example_images')