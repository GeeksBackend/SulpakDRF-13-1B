from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPI

router = DefaultRouter()
router.register('users', UserAPI, "api_users")

urlpatterns = router.urls