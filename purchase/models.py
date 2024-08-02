from django.db import models
from django.contrib.auth.models import User
from mango.models import MangoModel
# Create your models here.
ORDER_STATUS = (
    ('pending', 'pending'),
    ('running', 'running'),
    ('completed', 'completed'),
    ('cancelled', 'cancelled'),
)



class AddressModel(models.Model):
    city=models.CharField(max_length=20)
    street=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    def __str__(self):
        return self.city


class PurchaseModel(models.Model):
    mango=models.ForeignKey(MangoModel,on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(max_length=10,choices=ORDER_STATUS,default="pending")
    address=models.ForeignKey(AddressModel,null=True,blank=True,on_delete=models.SET_NULL)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.order_status

RATING=(
    ('🌟','🌟'),
    ('🌟🌟','🌟🌟'),
    ('🌟🌟🌟','🌟🌟🌟'),
    ('🌟🌟🌟🌟','🌟🌟🌟🌟'),
    ('🌟🌟🌟🌟🌟','🌟🌟🌟🌟🌟'),
)

class Review(models.Model):
    mango=models.ForeignKey(MangoModel,on_delete=models.SET_NULL,null=True,blank=True)
    reviewer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    body=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=10,choices=RATING)
    def __str__(self):
        return str(self.rating)


