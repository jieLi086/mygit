from django.db import models

# Create your models here.
class Infos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    class Meta:
        db_table = 'infos'
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'users'
