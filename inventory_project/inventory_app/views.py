from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import Product




class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   





