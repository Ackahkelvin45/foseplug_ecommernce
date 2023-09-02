from rest_framework import serializers
from .models import Wishlist
from listing.serializers import ViewListingSerializer


       
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        fields="__all__"



class ViewWishlistSerializer(serializers.ModelSerializer):
    listing=ViewListingSerializer()
    class Meta:
        model=Wishlist
        fields='__all__'