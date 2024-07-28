
from rest_framework import serializers
from . import models

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ContactModel
        fields="__all__"