from . import models

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CategoryModel
        fields='__all__'


class MangoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.MangoModel
        fields='__all__'



        