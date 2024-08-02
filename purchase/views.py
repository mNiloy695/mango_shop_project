from django.shortcuts import render
from rest_framework.response import Response
from . import serializers
from rest_framework import permissions
from rest_framework.views import APIView
# Create your views here.
from . import models
from rest_framework import viewsets
from rest_framework import filters

class PurchaseModelFilterForSpecificUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id=request.query_params.get('user_id')
        if user_id:
            return queryset.filter(user=user_id)
        return queryset

class PurchaseSerializerViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset=models.PurchaseModel.objects.all()
    serializer_class=serializers.PurchaseModelSerializer
    filter_backends=[PurchaseModelFilterForSpecificUser,filters.SearchFilter]
    search_fields=['PurchaseModel__id']

class ReviewFilterForSpecificMango(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        mango_id=request.query_params.get('mango_id')
        if mango_id:
            return queryset.filter(mango=mango_id)
        return queryset
class ReviewSerializerViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewModelSerializer
    filter_backends=[ReviewFilterForSpecificMango]


class AddressFilterForSpecificUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id=request.query_params.get('user_id')
        if user_id:
            return queryset.filter(user_id=user_id)
        return queryset
class AddressViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=serializers.AddressSerializer
    queryset=models.AddressModel.objects.all()
    filter_backends=[filters.SearchFilter,AddressFilterForSpecificUser]
    search_fields=['addressmodel__id','addressmodel__user_id']



