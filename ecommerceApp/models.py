from django.db import models
from django.contrib.auth.models import User

# prob we'll need some categories but they're optional
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # automatically set
    updated_at = models.DateTimeField(auto_now=True) # same

    # for a pleasant shell display of objects    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'), # if in cart
        ('COMPLETED', 'Completed'), # if confirmed
        ('CANCELLED', 'Cancelled'), # if cancelled
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    @property # so we can do order.total_price instead of order.total_price().
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# Each order can have multiple products, and one orderitem can be multiple products of the same type
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.price_at_purchase

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
