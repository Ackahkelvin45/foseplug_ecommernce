from django.shortcuts import render
from .serializers import ListingSerializer,StoreSerializer,CatergorySerializer,ViewListingSerializer
from .models import Listing,Category,Store
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from rest_framework.permissions import IsAuthenticated
from .filters import ListingFilter
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
import time




# Create your views here.

class ListingApiView(generics.ListAPIView):
   
    queryset=Listing.objects.all().order_by('-id')
    serializer_class=ViewListingSerializer
    filterset_class=ListingFilter
    def list(self, request, *args, **kwargs):  # Simulate a 5-second delay
        return super().list(request, *args, **kwargs)





class ListingDetailView(RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ViewListingSerializer
    lookup_field = 'pk'


@api_view(['POST','GET'])
def createListing(request):
    serilizer=ListingSerializer(data=request.data)
    if serilizer.is_valid():
        product=serilizer.save()

        return Response({
            "message": "Product created successfully",
        })
    return Response({
        "error": serilizer.errors
    })




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createStore(request):
    serilizer=StoreSerializer(data=request.data)
    if serilizer.is_valid():
        store=serilizer.save()

        return Response({
            "message": "store created successfully",
        })
    return Response({
        "error": serilizer.errors
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllStores(request):
    user=request.user
    stores=Store.objects.filter(owner_id=user.id)
    serializer=StoreSerializer(stores,many=True)
    return Response(
        {
            "store":serializer.data
        }
    )



@api_view(['GET'])
def getCategories(request):
    categories=Category.objects.all()
    serializer=CatergorySerializer(categories,many=True)
    return Response(
        {
            "categories":serializer.data
        }
    )






@api_view(['GET'])
def getTotalAds(request,pk):
    store=Store.objects.get(id=pk)
    listing=Listing.objects.filter(store_id=pk).count()
    return Response(
        {
            "count":listing
        }
    )




@api_view(['GET'])
def getRecommendedAds(request,pk):
    store=Store.objects.get(id=pk)
    listing=Listing.objects.filter(store_id=pk)
    serializer=ViewListingSerializer(listing,many=True)
    return Response(
        {
            "recommendedads":serializer.data
        }
    )

