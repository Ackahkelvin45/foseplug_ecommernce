from rest_framework import serializers
from .models import  Listing,Image,Category,Store,Subcategory
from django.utils import timezone
from humanize import naturaltime
from authentication.serializers import UserSerializer
from review.serializers import ReviewSerializer





class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields="__all__"


class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Subcategory
        fields="__all__"



class ListingSerializer(serializers.ModelSerializer):
    images=ImageSerializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    class Meta:
        model=Listing
        fields=['uploaded_images','title','images','description','subcategory','store',"price",'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Calculate the time difference and replace the original created value
        created_time_difference = naturaltime(timezone.now() - instance.created)
        representation['created'] = created_time_difference

        return representation
    def create(self, validated_data):
        pictures_data = validated_data.pop('uploaded_images')
        listing = Listing.objects.create(**validated_data)
       
        
        

        for picture_data in pictures_data:
            image=Image.objects.create(image=picture_data,products=listing)
            
            
        

        return listing
    

    

class StoreSerializer(serializers.ModelSerializer):
    owner=UserSerializer()
    class Meta:
        model=Store
        fields="__all__"



class ViewListingSerializer(serializers.ModelSerializer):
    images=ImageSerializer(many=True,read_only=True)
    category=CatergorySerializer()
    subcategory=SubCategorySerializer()
    store=StoreSerializer()
    review=ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model=Listing
        fields='__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Calculate the time difference and replace the original created value
        created_time_difference = naturaltime(timezone.now() - instance.created)
        representation['created'] = created_time_difference

        return representation
  



