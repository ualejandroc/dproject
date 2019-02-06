# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Custommer(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=10)
    edge= models.IntegerField()
    birth= models.DateField()
    document= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return '{}'.format(self.name)



class Application(models.Model):
    custommer= models.ForeignKey(Custommer,null=True, blank=True) 
    custommer_code=models.IntegerField()
    reazon=models.CharField(max_length=100)
    