from django.db import models

# Create your models here.
class Url(models.Model): # модель БД
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)