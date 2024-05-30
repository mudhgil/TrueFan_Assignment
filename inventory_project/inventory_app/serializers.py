from rest_framework import serializers
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Product
        fields = ['name', 'category', 'price']