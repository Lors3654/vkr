from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('current-user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('<slug:category_slug>/', CategoryAPIView.as_view(), name='categories'),
    path('latest-products/', LatestProductsList.as_view(), name='latest-products'),
    path('categories/<slug:category_slug>/', ProductsList.as_view()),
    path('search/', search),
    
]