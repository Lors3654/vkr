from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils.html import mark_safe

from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS_CHOICE = (
    ("process", "Processing"),
    ("paid", "Paid"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
    ("cancelled", "Cancelled"),
)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='phone')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created',
        help_text='date of user registration'
    )

    REQUIRED_FIELDS = ['name', 'lastname', 'phone']

    def __str__(self):
        return f"{self.name} {self.lastname}"

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to="category/")

    class Meta:
        verbose_name_plural = "Categories"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='product name', unique=True)
    slug = models.SlugField()
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='full description'
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    collection_name = models.CharField(max_length=255, verbose_name='collection')
    price = models.DecimalField(
        decimal_places=0,
        max_digits = 100,
        default=0,
        verbose_name='price'
    )
    stock_quantity = models.IntegerField(
        default=10,
        verbose_name='stock',
        help_text='available product stock'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created',
        help_text='timestamp when product was created'
    )
    image = models.ImageField(upload_to='uploads/')

    class Meta:
        ordering = ('-created_at',)
    
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return f"{self.product_name} - {self.category}"
    
    def get_absolute_url(self):
        return f"/{self.category.slug}/"
    
class ProductImage(models.Model):
    images = models.ImageField(upload_to='product-images/')
    category = models.ForeignKey(Category, related_name='product_images', on_delete=models.CASCADE, verbose_name='category', default=1)
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE, verbose_name='product')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='added',
        help_text='timestamp when image was added'
    )


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of addition')
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        ordering = ('-order_date',) 

    def __str__(self):
        return f"[ORDER {self.id}] - {self.user}" 


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(decimal_places=0, max_digits=100)
    total_amount = models.DecimalField(decimal_places=0, max_digits = 100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = self.quantity * self.unit_price
        super(OrderDetails, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Order Details"

    def __str__(self):
        return f"{self.product.product_name} x {self.quantity}"

class Favorite(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=('created'),
        help_text=('timestamp when the product was added in Favorites')
    )

