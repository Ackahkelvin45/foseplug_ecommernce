from rest_framework import serializers
from .models import CartIten
from listing.serializers import ViewListingSerializer


       
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartIten
        fields="__all__"



class ViewCartSerializer(serializers.ModelSerializer):
    listing=ViewListingSerializer()
    class Meta:
        model=CartIten
        fields='__all__'