from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description',]
    ordering_fields = ['id', 'title', 'description', 'quantity', 'price']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['products__id', 'products__title', 'products__description']
    ordering_fields = ['id', 'address', 'products']