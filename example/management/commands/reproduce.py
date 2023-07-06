import os
from django.core.management.base import BaseCommand, CommandError

from example.models import ExampleModel
from django.core.files.uploadedfile import SimpleUploadedFile

from mysite import settings


def file_for(path):
    """Gives you something you can pass into an models image field from a path to a file"""
    with open(path, 'rb') as file:
        return SimpleUploadedFile(
            name=os.path.basename(path),
            content=file.read(),
            content_type='image/jpeg',
        )


class Command(BaseCommand):
    help = "Reproduce an issue"

    def handle(self, *args, **options):
        print('reproduce')
        ExampleModel.objects.all().delete()
        print('deleted all example models')
        example = ExampleModel.objects.create(name='example', image=file_for('example_image.jpg'))
        print('created example model')
        thumbnail = example.image.thumbnail['400x400'].name
        thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail)
        print('created thumbnail', thumbnail_path)
        print('thumbnail exists?', os.path.exists(thumbnail_path))
        example.image.delete_all_created_images()
        print('ran delete_all_created_images()')
        example.image.delete(save=False)
        example.save()
        if os.path.exists(thumbnail_path):
            print('OH NO, thumbanil still exists!')
        else:
            print('all is well, thumbnail was removed')