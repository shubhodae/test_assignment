from django.db import models
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
