from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework  import status
from .serializers import RegisterSerializer,UserSerializer
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from listing.models import Store,Listing





# Create your views here.
@api_view(['post',])
def register_user(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        email=EmailMessage(
            "Thank you for registering",
            "You have successfully registered to fooseplug.com ,we hope you have a good experience!,Thank you",
             settings.EMAIL_HOST_USER,
            [
                user.email,
            ]
        )
        email.fail_silently = False
        email.send()

        
        data={
            "email": user.email,
            'success':"successfully registered",
        }

    else:
        data={
            "error":serializer.errors,
        }

    return Response(data)




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['other_names'] = user.other_names
        token['email'] = user.email

        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    user=request.user
    serializer=UserSerializer(user)
    stores=Store.objects.filter(owner_id=user.id)
    
    ads=0
    for store in stores:
        ads=ads+Listing.objects.filter(store_id=store.id).count()
        

    return Response({
        "user":serializer.data,
        'total_stores':Store.objects.filter(owner_id=user.id).count(),
        "total_ads":ads,
    })
