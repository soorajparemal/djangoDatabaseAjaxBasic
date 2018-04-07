from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)

    def __unicode__(self):
        return (self.name)