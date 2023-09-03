from django.urls import path
from . import views


app_name = 'reviews'


urlpatterns = [
    path('create_review/',views.create_review,name='review_create'),
    path("all_reviews/<int:pk>",views.get_reviews,name='all_review')
]