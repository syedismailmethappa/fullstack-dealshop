from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    store = serializers.ChoiceField(choices=Product.STORE_CHOICES)
    affiliateLink = serializers.URLField(source='affiliate_link')
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image', 'store', 'affiliateLink', 'category', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']



