from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory_app import views

router = DefaultRouter()
router.register('product', views.ProductViewset, basename= 'product')


urlpatterns = [

    path('', include(router.urls)),
    
]
