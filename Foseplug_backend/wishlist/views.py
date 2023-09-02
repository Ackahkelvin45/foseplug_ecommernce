from django.shortcuts import render
from .serializers import WishlistSerializer,ViewWishlistSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist

# Create your views here.



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToWishlist(request):
    serilizer=WishlistSerializer(data=request.data)
    if serilizer.is_valid():
        wishlistitem=serilizer.save()
        user=request.user
        allwishlisitems=Wishlist.objects.filter(user_id=user.id).count()

        return Response({
            "message": "item added to wishlist",
            "allwishlistitems":allwishlisitems
        })
    return Response({
        "error": serilizer.errors
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWishlistItems(request):
    user=request.user
    wishlistitems=Wishlist.objects.filter(user_id=user.id).order_by('-id')
    items=[]
    for cart in wishlistitems:
        items.append(cart.listing.id)

    serializer=ViewWishlistSerializer(wishlistitems,many=True)
    
    return Response(
        {
            "wishlistitems":serializer.data,
            'itemid':items
            
        }
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteWishlistItem(request,pk):
    wishlistitem=Wishlist.objects.get(pk=pk)
    wishlistitem.delete()
    user=request.user
    allwishlistitems=Wishlist.objects.filter(user_id=user.id).count()

    return Response(
        {
            "message":"item deleted successfully",
            'allwishlistitems': allwishlistitems
           
            
        }
    )

