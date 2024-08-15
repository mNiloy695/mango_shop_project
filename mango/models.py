from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class CategoryModel(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangoModel(models.Model):
    image=models.CharField(max_length=500,blank=True,null=True)
    title=models.CharField(max_length=100)
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    weight=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    def __str__(self):
        return self.title




    


