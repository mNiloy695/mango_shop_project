from django.db import models

# Create your models here.

class ContactModel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    country=models.CharField(max_length=100)
    body=models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.phone)