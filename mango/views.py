from django.shortcuts import render
from rest_framework import filters
# Create your views here.
from . import serializers
from rest_framework import viewsets
from . import models
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
class CategorySerializerViewSet(viewsets.ModelViewSet):
    queryset=models.CategoryModel.objects.all()
    serializer_class=serializers.CategorySerializer

class CategorySpecificMangoViewSet(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        category_id=request.query_params.get('category_id')
        if category_id:

            return queryset.filter(category_id=category_id)
        return queryset



class MangoPagination(PageNumberPagination):
    page_size=15
    page_size_query_param=page_size
    max_page_size=20
class MangoSerializerViewSet(viewsets.ModelViewSet):
    queryset=models.MangoModel.objects.all()
    pagination_class=MangoPagination
    serializer_class=serializers.MangoSerializer
    filter_backends=[filters.SearchFilter,CategorySpecificMangoViewSet]
    search_fields=['mangomodel__title','mangomodel__id','mangomodel__category_id']


# view for purchase Model



        





