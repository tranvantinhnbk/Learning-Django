from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class KhaoSat(models.Model):
    id = models.AutoField(primary_key=True)
    Cau1 = models.BooleanField(default=False)
    Cau2 = models.BooleanField(default=False)
    Lydo_Cau2 = models.CharField(max_length = 300, default = '')
    Cau3 = models.BooleanField(default=False)
    Lydo_Cau3 = models.CharField(max_length = 300, default = '')
    Cau4 = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Information(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    generation = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
