from django.urls import path 
from . import views

app_name='cart'


urlpatterns=[
    path('add_to_cart/',views.addTocart,name='add_to_cart'),
    path('cart_items/',views.getCartItems,name='cart_items'),
    path('delete_from_cart/<int:pk>',views.deleteCartItem,name='delete_from_cart'),
]