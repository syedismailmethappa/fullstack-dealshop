from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
      re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),

]

