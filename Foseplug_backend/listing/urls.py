from django.urls import path
from . import views
from .views import ListingApiView


app_name='listing'


urlpatterns=[
path("",ListingApiView.as_view(),name='alllisting'),
path("create/",views.createListing,name='createList'),
path('create-store/',views.createStore,name='createStore'),
path("allstores/",views.getAllStores,name='allStores'),
path('categories/',views.getCategories,name='categories'),


]