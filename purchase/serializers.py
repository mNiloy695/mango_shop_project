
from rest_framework import serializers
from . import models
# placing order for mango re vai

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AddressModel
        fields='__all__'
class PurchaseModelSerializer(serializers.ModelSerializer):
    # mango=serializers.StringRelatedField(many=False)
    # order_status=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.PurchaseModel
        fields='__all__'
    
    def save(self):
        mango=self.validated_data["mango"]
        user=self.validated_data["user"]
        order_status=self.validated_data["order_status"]
        quantity=self.validated_data["quantity"]
        price=mango.price * quantity
        address=self.validated_data['address']
        
        if quantity>mango.weight:
            raise serializers.ValidationError({'error':"Our Stock is low"})
        if quantity<2:
            raise serializers.ValidationError({'error':"You need to buy at least 2 kg"})
        
        purchase=models.PurchaseModel(mango=mango,user=user,order_status=order_status,quantity=quantity,price=price,address=address)
        man=models.MangoModel.objects.get(id=mango.id)
        

        if  purchase.order_status=="pending":
            man.weight-=purchase.quantity
            man.save()
        elif purchase.order_status =="cancelled":
            man.weight+=purchase.quantity
            man.save()


# review  serializer

class ReviewModelSerializer(serializers.ModelSerializer):
    reviewer=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Review
        fields='__all__'