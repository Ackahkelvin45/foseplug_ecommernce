from django.db import models
from listing.models import Listing
from authentication.models import User
from django.db.models import Avg

# Create your models here.


class Review(models.Model):
    text=models.TextField(max_length=400, blank=True,null=True)
    listing=models.ForeignKey(Listing, null=True,on_delete=models.SET_NULL,related_name='review')
    owner=models.ForeignKey(User, null=True, on_delete=models.SET_NULL,related_name='review_owner')
    rating=models.FloatField(null=True, default=0)
    average_rate=models.FloatField(null=True, default=0)
     

    def __str__(self):
        return self.text

    def calculate_average_rating(self):
        # Use the Avg aggregation function to calculate the average rating
        average_rating = Review.objects.filter(listing_id=self.listing.id).aggregate(Avg('rating'))['rating__avg']
        self.average_rate = average_rating
        
        
        # Check if there are reviews and an average rating exists
        if average_rating is not None:
            return round(average_rating, 2)  # Round the average rating to 2 decimal places
        else:
            return 0.0  # Default to 0 if there are no reviews

    
