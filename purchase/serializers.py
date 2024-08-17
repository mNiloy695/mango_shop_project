
from rest_framework import serializers
from . import models
# placing order for mango re vai

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AddressModel
        fields='__all__'
class PurchaseModelSerializer(serializers.ModelSerializer):
    mango=serializers.StringRelatedField(many=False)
    # order_status=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.PurchaseModel
        fields='__all__'


# review  serializer

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Review
        fields='__all__'