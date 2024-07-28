from django.shortcuts import render
from rest_framework  import permissions


# Create your views here.
from . import models
from  rest_framework import viewsets
from .  import serializers
class ContactViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset=models.ContactModel.objects.all()
    serializer_class=serializers.ContactSerializer

    
