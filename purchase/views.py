from django.shortcuts import render
from rest_framework.response import Response
from . import serializers
from rest_framework import permissions
from rest_framework.views import APIView
# Create your views here.
from . import models
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from django.http import Http404
from mango.models import MangoModel
class PurchaseModelFilterForSpecificUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id=request.query_params.get('user_id')
        if user_id:
            return queryset.filter(user=user_id)
        return queryset

class PurchaseSerializerViewSet(APIView):
   def get(self,request,format=None):   
       print("get method")
       purchases=models.PurchaseModel.objects.all()
       serializer=serializers.PurchaseModelSerializer(purchases,many=True)
       return Response(serializer.data)
   def post(self,request,format=None):
       purchase=request.data
       serializer=serializers.PurchaseModelSerializer(data=purchase)
       if serializer.is_valid():
           mango=serializer.validated_data.get('mango')
           print(mango)
        #    mango=MangoModel.objects.get(id=id)
           quantity=serializer.validated_data.get('quantity')
           order_status=serializer.validated_data.get('order_status')
           if(order_status=="pending"):
               mango.weight-=quantity
               mango.save()
                   
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PurchaseDetails(APIView):
    def get_object(self,pk):
        try:
            return models.PurchaseModel.objects.get(pk=pk)
        except models.PurchaseModel.DoesNotExist:
            return Http404
    def get(self,request,pk,fomate=None):
        purchase=self.get_object(pk)
        serializer=serializers.PurchaseModelSerializer(purchase)
        return Response(serializer.data)
    def put(self,request,pk,fomate=None):
        purchase=self.get_object(pk)
        serializer=serializers.PurchaseModelSerializer(purchase,data=request.data)
        if serializer.is_valid():
            
            mango=serializer.validated_data.get('mango')
            order_status=serializer.validated_data.get('order_status')
            print(purchase.order_status)
            print(order_status)
            if(purchase.order_status!="cancelled" and order_status=="cancelled"):
               mango.weight+=purchase.quantity
               mango.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,formate=None):
        purchase=self.get_object(pk)
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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



