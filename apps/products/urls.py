from django.urls import path 

from apps.products.views import ProductListAPI, ProductCreateAPI, ProductUpdateAPI, ProductDestroyAPI

urlpatterns = [
    path('', ProductListAPI.as_view(), name="api_products"),
    path('create/', ProductCreateAPI.as_view(), name="api_products_create"),
    path('update/<int:pk>/', ProductUpdateAPI.as_view(), name="api_products_update"),
    path('destroy/<int:pk>/', ProductDestroyAPI.as_view(), name="api_product_destroy")
]