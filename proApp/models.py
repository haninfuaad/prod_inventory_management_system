from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class inventoryModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    created_at=models.DateField(auto_now_add=True)