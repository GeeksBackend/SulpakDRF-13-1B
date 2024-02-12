from rest_framework.generics import ListAPIView

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

# Create your views here.
class CategoryListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer