from rest_framework import serializers
from .models import *
import logging

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('images', 'created_at')

class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "product_name",
            "get_absolute_url",
            "description",
            "category",
            "collection_name",
            "price",
            "stock_quantity",
            "created_at",
            "image",
            "product_images"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "image",
            "products",
        )

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product_status']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderDetails
        fields = '__all__'

class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderDetails
        fields = (
            "product",
            "quantity",
            "unit_price",
            "total_amount"
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'order_date',
            'product_status',
            'items'
        )

class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'product', 'created_at']
