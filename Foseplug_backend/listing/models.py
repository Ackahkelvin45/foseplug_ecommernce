from django.db import models
from authentication.models import User

# Create your models here.

OPTIONS=(
    ('MEN','men'),
    ("FEMALE",'female'),
    ('KIDS','kids'),
    ("UNISEX",'unisex'),
)




class Store(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(max_length=300,null=True,blank=True)
    owner=models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name




class Subcategory(models.Model):
    name=models.CharField(max_length=100,choices=OPTIONS,null=True)

    def __str__(self) :
        return self.name





class Category(models.Model):

    name=models.CharField(max_length=50, unique=True,null=True,)
    icon=models.ImageField(null=True, blank=True,upload_to='category/')

    def __str__(self):
        return self.name



class Listing(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    category=models.ForeignKey(Category, null=True,blank=True, on_delete=models.SET_NULL,related_name='product_category')
    subcategory=models.ForeignKey(Subcategory, null=True, blank=True,on_delete=models.SET_NULL,related_name='product_subcategory')
    description=models.TextField(null=True, blank=True, )
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)
    store=models.ForeignKey(Store, null=True, blank=True,on_delete=models.CASCADE,related_name='product_store')
    price=models.FloatField(null=True)

    def __str__(self):
        return str(self.title)
     
class Image(models.Model):
    image=models.ImageField(null=True, blank=True,upload_to='productsimages/')
    products=models.ForeignKey(Listing,null=True, on_delete=models.CASCADE,related_name='images')

    def __str__(self) :
        return str(self.products)



    
class FavoriteListing(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL,related_name='owner_list')
    listing=models.OneToOneField(Listing,null=True, on_delete=models.SET_NULL,related_name='fav_item')

    def __str__(self):
        return self.listing.title







    