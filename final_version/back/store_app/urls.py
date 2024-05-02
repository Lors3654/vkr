from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('current-user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('orders/', OrderCreateView.as_view(), name='user-orders'), 
    path('checkout/', checkout, name='checkout'), 
    path('my-orders/', UserOrdersView.as_view(), name='my-orders'),
    path('favorites/', get_favorites, name='get-favorites'),
    path('favorites/add/', add_to_favorites, name='favorites'),
    path('favorites/<int:favorite_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('latest-products/', LatestProductsList.as_view(), name='latest-products'),
    path('categories/<slug:category_slug>/', ProductsList.as_view()),
    path('<slug:category_slug>/', CategoryAPIView.as_view(), name='categories'),
    path('search/', search, name='search'),
    
    
    
]