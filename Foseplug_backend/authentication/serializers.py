from .models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True,)
    class Meta:
        model=User
        fields=('email', 'password')

    def create(self,validated_data):
        user = User.objects.create(email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()

        return user
      







