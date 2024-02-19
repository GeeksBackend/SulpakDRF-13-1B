from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, "api_categories")

urlpatterns = router.urls