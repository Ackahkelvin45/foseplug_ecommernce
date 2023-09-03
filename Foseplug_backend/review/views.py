from django.shortcuts import render
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Review

# Create your views here.


@api_view(['POST'])
def create_review(request):
    data = request.data
    serializer=ReviewSerializer(data=data)
    if serializer.is_valid():
        review=serializer.save()
        review.calculate_average_rating()
        review.owner=request.user
        review.save()
        
        return Response({
            "message": "success",
        })
    return Response ({
        "message":serializer.errors
    })



@api_view(['GET',])
def get_reviews(request,pk):
    reviews = Review.objects.filter(listing_id=pk)
    serializer=ReviewSerializer(reviews,many=True)
    return Response({
        "reviews": serializer.data,
    })


