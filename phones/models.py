from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# --- BRAND MODEL ---
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name

# --- PRODUCT MODEL (Mobiles, Laptops, Tablets, TVs) ---
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('mobile', 'Mobile'),
        ('laptop', 'Laptop'),
        ('tablet', 'Tablet'),
        ('tv', 'TV'),
    ]

    STORE_CHOICES = [
        ('amazon', 'Amazon'),
        ('flipkart', 'Flipkart'),
        ('reliance', 'Reliance Digital'),
        ('other', 'Other Store'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='mobile')
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, 
        related_name='products'
    )
    name    = models.CharField(max_length=200)
    slug    = models.SlugField(unique=True, blank=True, null=True)
    price   = models.IntegerField()
    
    # Specs (Inhe blank=True rakha hai kyunki TV/Laptop ke specs alag ho sakte hain)
    ram     = models.IntegerField(help_text="RAM in GB", blank=True, null=True)
    storage = models.IntegerField(help_text="Storage in GB", blank=True, null=True)
    battery = models.IntegerField(help_text="Battery in mAh", blank=True, null=True)
    camera  = models.IntegerField(help_text="Main Camera in MP", blank=True, null=True)
    processor = models.CharField(max_length=100, blank=True)
    
    description = models.TextField(blank=True)
    image   = models.ImageField(upload_to='products/', blank=True)
    
    # Affiliate Fields
    buy_url = models.URLField(max_length=500, blank=True, null=True, help_text="Store link yahan daalein")
    store_name = models.CharField(max_length=20, choices=STORE_CHOICES, default='amazon')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Slug mein category bhi add kar sakte hain unique rakhne ke liye
            self.slug = slugify(f"{self.category}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.brand.name} {self.name}"

