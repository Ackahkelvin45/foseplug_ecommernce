from django.shortcuts import render
from .serializers import CartSerializer,ViewCartSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CartIten

# Create your views here.



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTocart(request):
    serilizer=CartSerializer(data=request.data)
    if serilizer.is_valid():
        cartitem=serilizer.save()
        user=request.user
        allcartitems=CartIten.objects.filter(user_id=user.id).count()

        return Response({
            "message": "item added to cart",
            "allcartitems":allcartitems
        })
    return Response({
        "error": serilizer.errors
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCartItems(request):
    user=request.user
    cartitems=CartIten.objects.filter(user_id=user.id).order_by('-id')
    items=[]
    for cart in cartitems:
        items.append(cart.listing.id)

    serializer=ViewCartSerializer(cartitems,many=True)
    
    return Response(
        {
            "cartitems":serializer.data,
            'itemid':items
            
        }
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteCartItem(request,pk):
    cartitem=CartIten.objects.get(pk=pk)
    cartitem.delete()
    user=request.user
    allcartitems=CartIten.objects.filter(user_id=user.id).count()

    return Response(
        {
            "message":"item deleted successfully",
            'allcartitems': allcartitems
           
            
        }
    )

