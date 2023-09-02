from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework  import status
from .serializers import RegisterSerializer
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




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
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    