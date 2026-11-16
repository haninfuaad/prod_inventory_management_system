from rest_framework import serializers
from proApp.models import inventoryModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=inventoryModel
        fields="__all__"
        read_only_fields=['owner','id','created_at']

    stock_status=serializers.SerializerMethodField()

    def get_stock_status(self,obj):
        if obj.stock==0:
            return "out of stock"

        elif 1 <= obj.stock <= 10:
            return "low stock"

        elif obj.stock>10:
            return "available"

    def validate_price(self, k):
        if k<0:
            raise serializers.ValidationError(
                "negative price!!"
            )
        return k