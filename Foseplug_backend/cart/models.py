from django.db import models
from authentication.models import User
from listing.models import Listing


# Create your models here.



class CartIten(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL,related_name='owner_cart')
    listing=models.OneToOneField(Listing,null=True, on_delete=models.SET_NULL,related_name='cart_item')
    quantity=models.IntegerField(null=True,blank=True,default=1)

    def __str__(self):
        return self.listing.title