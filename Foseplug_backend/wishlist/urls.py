from django.urls import path 
from . import views

app_name='wishlist'


urlpatterns=[
    path('add_to_wishlist/',views.addToWishlist,name='add_to_wishlist'),
    path('wishlist_items/',views.getWishlistItems,name='wishlist_items'),
    path('delete_from_wishlist/<int:pk>',views.deleteWishlistItem,name='delete_from_wishlist'),
]

