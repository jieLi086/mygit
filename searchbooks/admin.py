from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
#注册模型
admin.site.register(models.Users)
admin.site.register(models.Infos)