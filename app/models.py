from django.db import models
from django.contrib.auth.models import User


class Medicines(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    MedicinesName = models.CharField(max_length=30)
    Quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    Price = models.IntegerField()

