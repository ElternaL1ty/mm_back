from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, UserSerializer
from .models import Category, Product, Order
from rest_framework import filters, request
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ('get',)


class ProductViewSet(ModelViewSet):
    filterset_fields = ['id', 'categories']
    search_fields = ['name', 'desc']
    ordering_fields = ('name', 'price')
    ordering = ('name')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ('get',)
    pagination_class = ProductPagination


class OrderViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-create_date')
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get','post')


class UserViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ('get','post', 'put')