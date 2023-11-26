from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from .manager import UserManager

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Beauty & Skin Care', 'Beauty & Skin Care'),
        ('Clothing', 'Clothing'),
        ('Home & Kitchen', 'Home & Kitchen'),
        ('Accessories', 'Accessories'),
        # Add more choices as needed
    ]
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    slug = models.SlugField()
    def __str__(self):
        return self.title
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    USERNAME_FIELD = 'username'
    objects = UserManager()

class ItemInventory(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.item.title

class CartObject(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.item.title

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemInventory)
    # ordered_date = models.DateTimeField()
    ordered_date = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    def __str__(self):
        return self.user.username


