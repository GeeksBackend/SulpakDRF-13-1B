from django.urls import path 

from apps.categories.views import CategoryListAPI, CategoryCreateAPI, CategoryUpdateAPI, CategoryDestroyAPI

urlpatterns = [
    path('', CategoryListAPI.as_view(), name="api_categories"),
    path('create/', CategoryCreateAPI.as_view(), name="api_categories_create"),
    path('update/<int:pk>/', CategoryUpdateAPI.as_view(), name="api_categories_update"),
    path('destroy/<int:pk>/', CategoryDestroyAPI.as_view(), name="api_categories_destroy")
]