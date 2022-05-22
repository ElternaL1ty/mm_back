from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, IntegerField, DateTimeField
from .models import Category, Product, Order
from rest_framework.validators import ValidationError
import datetime

class CategorySerializer(ModelSerializer):
    name = CharField(required=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    name = CharField(required=True)
    varcode = CharField(required=True)
    desc = CharField(required=False)
    price = IntegerField(required=True)
    amount = IntegerField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    status = CharField(default='Created')

    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'status', 'create_date', 'complete_date')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
