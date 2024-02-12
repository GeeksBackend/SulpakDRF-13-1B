from django.urls import path 

from apps.products.views import ProductListAPI

urlpatterns = [
    path('', ProductListAPI.as_view(), name="api_products")
]