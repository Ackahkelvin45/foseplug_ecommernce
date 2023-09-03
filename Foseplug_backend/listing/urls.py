from django.urls import path
from . import views
from .views import ListingApiView,ListingDetailView



app_name='listing'


urlpatterns=[
path("",ListingApiView.as_view(),name='alllisting'),
path("create/",views.createListing,name='createList'),
path('create-store/',views.createStore,name='createStore'),
path("allstores/",views.getAllStores,name='allStores'),
path('categories/',views.getCategories,name='categories'),
path('detail/<int:pk>/',ListingDetailView.as_view(),name='detail'),
path('storecounter/<int:pk>/',views.getTotalAds,name='storecount'),
path('recommended/<int:pk>/',views.getRecommendedAds,name='recommended'),


]