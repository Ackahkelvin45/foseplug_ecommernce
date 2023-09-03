from rest_framework import serializers
from .models import Review
from authentication.serializers import UserSerializer




class ReviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Review
        fields="__all__"
