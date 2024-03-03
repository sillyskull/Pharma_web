from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, Group, Permission


class Medicines(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    MedicinesName = models.CharField(max_length=30)
    Quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    Price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.MedicinesName
    
class User(AbstractBaseUser):
    # groups = models.ManyToManyField(Group, related_name= 'medicine_users')
    # user_permissions = models.ManyToManyField(Permission, related_name= 'medicine_users')
    pass
