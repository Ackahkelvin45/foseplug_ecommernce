import django_filters
from .models import Listing,Category,Subcategory,Store


class ListingFilter(django_filters.FilterSet):
   
    class Meta:
        model=Listing
        fields={'title':['icontains']
                ,'category__name':['icontains']
                ,'subcategory__name':['icontains']
                ,'price':['lt','gt'],
                'store__location':['icontains']}
