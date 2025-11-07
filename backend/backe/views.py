from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category']
    ordering_fields = ['created_at', 'price', 'title']
    ordering = ['-created_at']
    
    @action(detail=False, methods=['get'])
    def by_store(self, request):
        """
        Get products filtered by store.
        Usage: /api/products/by_store/?store=Flipkart
        """
        store = request.query_params.get('store', None)
        if store:
            products = Product.objects.filter(store=store)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "store parameter is required"}, status=400)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search products by title or category.
        Usage: /api/products/search/?q=shoes
        """
        query = request.query_params.get('q', '')
        if query:
            products = Product.objects.filter(
                models.Q(title__icontains=query) | 
                models.Q(category__icontains=query)
            )
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response([])
