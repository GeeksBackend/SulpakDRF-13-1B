from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

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
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'description', 'price')
    search_fields = ('title', 'description', 'price')

    def get_permissions(self):
        if self.action == "retrieve":
            return (IsAuthenticated(), )
        return (AllowAny(), )