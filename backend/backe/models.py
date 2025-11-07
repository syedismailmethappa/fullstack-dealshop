from django.db import models


class Product(models.Model):
    STORE_CHOICES = [
        ('Flipkart', 'Flipkart'),
        ('myntra', 'Myntra'),
        ('meesho', 'Meesho'),
    ]
        
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    image = models.URLField(max_length=1000, blank=True)
    store = models.CharField(max_length=20, choices=STORE_CHOICES)
    affiliate_link = models.URLField(max_length=1000)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
