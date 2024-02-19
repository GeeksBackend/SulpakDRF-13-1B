from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, "api_products")

urlpatterns = router.urls