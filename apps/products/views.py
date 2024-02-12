from rest_framework.generics import ListAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

# Create your views here.
class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer