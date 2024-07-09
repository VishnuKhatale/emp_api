from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    images = models.ImageField(upload_to='images',null=True)