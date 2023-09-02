from django.db import models
from listing.models  import Listing 
from authentication.models import User 

# Create your models here.
class Wishlist(models.Model):
    listing=models.OneToOneField(Listing,null=True,related_name='wishlist_item',on_delete=models.SET_NULL)
    user=models.ForeignKey(User,null=True,related_name='wishlist_user',on_delete=models.SET_NULL)
    
    def __str__(self):
        return  str(self.listing)


