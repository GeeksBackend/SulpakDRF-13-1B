from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

# Create your views here.
class ProductListAPI(ListAPIView): #GET
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPI(CreateAPIView): #POST
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPI(UpdateAPIView): #PUT, PATCH
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyAPI(DestroyAPIView): #DELETE
    queryset = Product.objects.all()