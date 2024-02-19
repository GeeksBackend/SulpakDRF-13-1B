from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer