from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import api_view
from rest_framework.generics import *
from .serializers import *
from .models import *
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

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
    
    def get_absolute_image_url(self, image_path):
        current_site = get_current_site(self.request)
        return f"http://{current_site.domain}{image_path}"
    
    def get(self, request, category_slug, format=None):
        category = self.get_category(category_slug)
        products = category.products.all()
        serialized_data = []
        for product in products:
            product_data = ProductSerializer(product).data
            product_data['image'] = self.get_absolute_image_url(product_data['image'])
            for product_image in product_data.get('product_images', []):
                product_image['images'] = self.get_absolute_image_url(product_image['images'])
            serialized_data.append(product_data)
        return Response(serialized_data)
    
class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

@api_view(['GET'])
def search(request):
    query = request.GET.get("q", "")
    if not query:
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    products = Product.objects.filter(product_name__icontains=query) | Product.objects.filter(description__icontains=query)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            logging.error(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def checkout(request):
    # Это предполагает, что заказ уже создан, и мы только добавляем элементы к нему.
    order_id = request.data.get('order')
    items_data = request.data.get('items')

    if not order_id or not items_data:
        return Response({"detail": "Order ID and items must be provided."}, status=status.HTTP_400_BAD_REQUEST)

    response_data = []
    errors = []

    for item in items_data:
        item['order'] = order_id  # Добавляем ID заказа к каждому элементу
        serializer = OrderItemSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
            response_data.append(serializer.data)
        else:
            errors.append(serializer.errors)

    if errors:
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(response_data, status=status.HTTP_201_CREATED)


class UserOrdersView(APIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        print("Orders data:", serializer.data) 
        return Response(serializer.data)

  
@api_view(['POST'])
def add_to_favorites(request):
    user = request.user
    product_id = request.data.get('product_id')
    print(f"Trying to find product with ID: {product_id}")
    product = get_object_or_404(Product, id=product_id)

    favorite_exists = Favorite.objects.filter(user=user, product=product).exists()
    if not favorite_exists:
        favorite = Favorite.objects.create(user=user, product=product)
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'This item is already in favorites'}, status=status.HTTP_409_CONFLICT)

@api_view(['GET'])
def get_favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def remove_from_favorites(request, favorite_id):
    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)