from django.contrib import admin

# Register your models here.

from django.contrib import admin
from example.models import ExampleModel


class ExampleAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExampleModel, ExampleAdmin)