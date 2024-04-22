from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import api_view
from rest_framework.generics import *
from .serializers import *
from .models import *

class CurrentUserAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class LatestProductsList(APIView):
     def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductsList(APIView):
    def get_category(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get_products(self, category_slug):
        category = self.get_category(category_slug)
        return category.products.all()
    
    def get_absolute_image_url(self, image_path):
        current_site = get_current_site(self.request)
        return f"http://{current_site.domain}{image_path}"
    
    def get(self, request, category_slug, format=None):
        products = self.get_products(category_slug)
        serialized_data = ProductSerializer(products, many=True).data
        for product_data in serialized_data:
            product_data['image'] = self.get_absolute_image_url(product_data['image'])
            for product_image in product_data.get('product_images', []):
                product_image['images'] = self.get_absolute_image_url(product_image['images'])
        return Response(serialized_data)
    
class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})