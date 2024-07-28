from typing import Any
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.MangoModel)
admin.site.register(models.CategoryModel)




